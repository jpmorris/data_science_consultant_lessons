# Recipes - Useful SQL Querries

## Create a copy of a table
Instead of creating a table from scratch, try and copy a similar one. This will 
```sql
CREATE TABLE new_table (LIKE old_table INCLUDING ALL);
INSERT INTO new_table
SELECT * FROM old_table; 
```
The `LIKE` keyword is used to copy the structure of the table. 
The `INCLUDING ALL` keyword is used to copy the constraints, indexes, defaults, etc. 
The `INSERT INTO` statement is used to copy the data from the old table to the new table.

However if you don't need all constraints, indexes etc this is sufficient:
```sql
CREATE TABLE new_table
SELECT * FROM old_table; 
```

## Get null fraction differences between two tables
```sql
with orig as (
    select attname, null_frac from pg_stats where schemaname = 'std' AND tablename = 'a133_general'
),
new as (
    select attname, null_frac from pg_stats where schemaname = 'raw' AND tablename = 'general'
)

select 
    orig.attname,
    orig.null_frac as orig_nf,
    new.null_frac as new_nf,
    orig.null_frac - new.null_frac as diff,
    CASE
        WHEN (orig.null_frac - new.null_frac)/nullif(new.null_frac,0) is not null
        THEN (orig.null_frac - new.null_frac)/nullif(new.null_frac,0)
        ELSE 0
    END AS per_diff,
    ((orig.null_frac = 0 AND new.null_frac > 0.15) OR ((orig.null_frac - new.null_frac)/nullif(new.null_frac,0) > 0.15)) AND (new.null_frac > 0.05) as poss_issue
from orig
left join new
    on orig.attname = new.attname
order by poss_issue desc
```

## Get SQL Processes that are blocked
This may need to be run from `psql` from the CLI if there is no access to other tools.
```sql
 select pid,
       usename,
       pg_blocking_pids(pid) as blocked_by,
       query as blocked_query
from pg_stat_activity
where cardinality(pg_blocking_pids(pid)) > 0;
```
## Terminate a query you own
```sql
SELECT pg_terminate_backend(<pid>);
```

## Get the size of a table

## Copy tables from one database to another
You need to use both `psql` and `pgdump` for this.
You'll also need to setup a `.pgpass` file to avoid passwords in history. 
```bash
pg_dump -s --host <source_host> --username <username> --no-password -t <schema.table>  <source_db> | psql --host <target_host> --username <username> --no-password <target_db>
```

## Get count of all types in database
```sql
select data_type, count(*) 
from information_schema.columns 
group by data_type
order by count DESC;
```

## Check for long-running queries
```sql
SELECT	
  pid,	
  now() - pg_stat_activity.query_start AS duration,	
  query,	
  state	
FROM pg_stat_activity	
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

## Collect statistics about table and store - useful to help query planner make better decisions
Should be run after (big) inserts.
```sql
ANALYZE <table>;
```

## Estimate row-count on a table
```sql
SELECT reltuples::bigint FROM pg_class WHERE oid = '<table>'::regclass; 
```

## Finding columns within tables within the database
```sql
select t.table_schema,
       t.table_name,
	   c.column_name
from information_schema.tables t
inner join information_schema.columns c on c.table_name = t.table_name
                                and c.table_schema = t.table_schema
where c.column_name like '%performance%'
      and t.table_schema not in ('information_schema', 'pg_catalog')
      and t.table_schema = 'std'  
	  and t.table_name = 'fpds_contracts'
order by t.table_schema;
```


