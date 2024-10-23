# Recipes - Useful SQL Querries

## Referencing an Aliased Column in a WHERE Clause
```sql
SELECT *
    FROM (
        SELECT column_name AS alias_name
        FROM table_name
    ) x
WHERE salary < 5000
```

## Conditional in SELECT statement:
```sql
select ename,sal,
    case when sal <= 2000 then 'UNDERPAID'
        then sal >= 4000 then 'OVERPAID'
        else 'OK'
    end as status
from emp
```

## Finding rows in common between two tables
```sql
select empno,ename,job,sal,deptno
from emp
where (ename,job,sal) in (
    select ename,job,sal from emp
    intersect
    select ename,job,sal from V
)
```

## Determining if two tables have the same data


## Identifying and avoiding Cartesian Products


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

## kill all idle querries:
```sql
WITH inactive_connections AS (
    SELECT
        pid,
        rank() over (partition by client_addr order by backend_start ASC) as rank
    FROM 
        pg_stat_activity
    WHERE
        -- Exclude the thread owned connection (ie no auto-kill)
        pid <> pg_backend_pid( )
    AND
        -- Exclude known applications connections
        application_name !~ '(?:psql)|(?:pgAdmin.+)'
    AND
        -- Include connections to the same database the thread is connected to
        datname = current_database() 

    AND
        -- Include inactive connections only
        state in ('idle', 'idle in transaction', 'idle in transaction (aborted)', 'disabled') 
    AND
        -- Include old connections (found with the state_change field)
        current_timestamp - state_change > interval '5 minutes' 
)
SELECT
    pg_terminate_backend(pid)
FROM
    inactive_connections 
WHERE
    rank > 1
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

## Get histogram from data
```sql


with diff as (
	select 
		g.grantee_id,
		g.latitude,
		esg2.latitude,
		g.longitude,
		esg2.longitude,
		abs(g.latitude - esg2.latitude) as lat_diff,
		abs(g.longitude - esg2.longitude) as long_diff
	from public.grantee g
	join std.esri_updated_geocode esg2 
	on g.grantee_id = esg2.tax_identifier_number::BIGINT 
	where abs(g.latitude - esg2.latitude) > 0 or abs(g.longitude - esg2.longitude) > 0
),
diff_stats as (
	select 
		min(lat_diff) as min,
		max(lat_diff) as max
	from diff
),
freq as (
	select 
		width_bucket(lat_diff, min, max, 10) as bucket,
        -- int4range if integer
        numrange(min(lat_diff), max(lat_diff)) as range,
		count(*)as freq
	from diff, diff_stats
	group by bucket
	order by bucket
)

select 
	bucket, 
	range, 
	freq,
   repeat('■',
          (   freq::float
            / max(freq) over()
            * 30
          )::int
   ) as bar
from freq
```

