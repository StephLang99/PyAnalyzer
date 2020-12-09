select 
a.name,
c.short_name,
b.value,
c.domain,
c.val_type
 from projects a
inner join project_measures b
on a.uuid = b.component_uuid
inner join snapshots d
on  b.analysis_uuid = d.uuid 
inner join metrics c
on c.uuid = b.metric_uuid
where d.islast = true

