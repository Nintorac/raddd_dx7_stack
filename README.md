## Lakh DX7 Render

Allows the reader to render the Lakh dataset using Dexed an emulator of the classic DX7. See the accompanying article at [nintoracaudio.com]() ## fill lionk https://www.nintoracaudio.dev/devops/2020/04/22/thiscartdoesnotexist.html

## Structure

```bash
.
├── data                        # where the data will end up
├── dghome                      # DAGSTER_HOME
│   └── dagster.yaml            #     
├── instruments                 # Put your synth here
├── raddd                       # 
│   └── __init__.py             # All the dagster code is here
├── raddd_dbt                   # 
│   ├── dbt_project.yml         # Main DBT configuration    
│   ├── models                  # 
│   │   ├── 4_beat_phrases.sql  # The 4 beat phrases are extracted here            
│   │   ├── render_midis.py     # UDF Implemented here        
│   │   ├── schema.yml          #     
│   │   └── sources.yml         # Configure the sources to point at hugging face    
│   ├── profiles.yml            # Can you attach postgres and write the outputs there?
└─  └── README.md               # 
```
## DBT

You can hack around with `dbt` by itself if you like, but really you should do everything through `dagster`

### Using the project

Try running the following commands:
- `dbt run --profiles-dir .`
- `dbt test --profiles-dir .`


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

#### Other related links
- https://github.com/duckdb/postgres_scanner/pull/111
- https://filesystem-spec.readthedocs.io/en/latest/
- https://duckdb.org/docs/api/python/overview.html#dataframes
- https://thenewstack.io/how-open-source-arrow-helps-solve-time-series-data-dilemmas/
- http://softwareengineeringdaily.com/wp-content/uploads/2022/03/SED1439-DuckDB-with-Hannes-Muhleisenpdf
- https://asb2m10.github.io/dexed/
- https://spotify.github.io/pedalboard/
- https://gitlab.com/nintorac-audio/midi_etl
- https://github.com/duckdb/dbt-duckdb
- https://huggingface.co/datasets/nintorac/midi_etl
- https://docs.getdbt.com/reference/source-configs
- https://github.com/duckdb/dbt-duckdb#reading-from-external-files
- https://duckdb.org/docs/extensions/httpfs.html
- https://github.com/asb2m10/dexed/releases/tag/v0.9.6
- https://duckdb.org/docs/api/python/relational_api.html
- https://github.com/dagster-io/dagster/issues/1890
- https://docs.dagster.io/concepts/partitions-schedules-sensors/backfills
- https://github.com/duckdb/duckdb/discussions/9607# s4_dx7
