with note_dicts as (
	SELECT
		floor(e.start_time/4) bucket
git
	FROM {{ source('midi', 'detailed_notes') }} e
	where midi_id like 'f%'
	order by e.track_id, e.start_time, e.note, e.duration, e.velocity asc
)
select 
	bucket
	, track_id
	, list(note) notes
	, ntile({{ var('n_partitions', 100 )}}) over () as p
from note_dicts
group by bucket, track_id
order by p
