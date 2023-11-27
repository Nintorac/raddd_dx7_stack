from itertools import chain
import os
from pathlib import Path
from dagster import Definitions, StaticPartitionsDefinition, with_resources, configured, AssetsDefinition
from dagster_dbt import load_assets_from_dbt_project
from dagster_dbt import dbt_cli_resource as dbt

project_root = Path(__file__).parent / '..'
dbt_project = (project_root / 'raddd_dbt').as_posix()
N_PARTITIONS = os.environ.get('N_PARTITIONS', 13332)

# Load static assets
assets = load_assets_from_dbt_project(
    dbt_project,
    profiles_dir=dbt_project,
    select='4_beat_phrases',
)


# Load partitioned assets
def partition_f(partition):
    return {'partition_n': int(partition)}

def metadata_fn(x):
    return {"partition_expr": "p"}

# list of strings for each partition
partitions_def = StaticPartitionsDefinition(list(map(str, range(1, 1+int(N_PARTITIONS)))))

partitioned_assets = load_assets_from_dbt_project(
    dbt_project,
    profiles_dir=dbt_project,
    select='render_midis',
    partitions_def=partitions_def,
    partition_key_to_vars_fn=partition_f,
    node_info_to_definition_metadata_fn=metadata_fn
)


assets = with_resources(
    chain(assets, partitioned_assets),
    resource_defs={
        'dbt': dbt.configured({
            'profiles_dir': dbt_project,
            'project_dir': dbt_project,
            'vars': {'n_partitions': N_PARTITIONS}
        }),
    }
)

defs = Definitions(
    assets=assets,
)
