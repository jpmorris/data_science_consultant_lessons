# Ways data scientists manipulate and process data:
- Pandas
- Numpy
- Polars
- Dask
- DuckDB
- Spark
- SQL
- Hadoop

# In-memory, single machine options
- Pandas - most widly supported dataframe library
- Numpy - multi-dimensional arrays, mostly numerical
- Dask - parallelized dataframes
- DuckDB - columnar-vectorized query engine with SQL interface
- Polars - parallized dataframes
- Vaex - Out-of-core DataFrames
- Modin - drop-in replacement for pandas, but parallelized


# In memory, distributed
- Apache Spark - analytics engine for large-scale data processing
- Lesser used (by data scientists)
  - Apache Flink - stream processing/batch procesing framework
  - Apache Beam - data procesing piplines


# On-disk, single machine
- SQL:
  - Goes back to 1970s; built on low-memory constriants
  - Many engines (SQLite, MySQL, Postgres, Oracle, SQL Server, etc.)
  - Computation happens on disk
     - memory usage is determined by `work_mem`, and is often very small (ours is at 4MB)
     - Units of work occur in memory but are written to disk and cleared from memory as needed
       - This is why you can run large queries on a small machine

# On disk, distributed
- Hadoop - distributed storage and processing
  - HDFS - distributed file system
  - MapReduce - distributed processing
  - Pig - SQL-like language on top of Hadoop
  - Hive - SQL-like language on top of Hadoop
  - HBase - key value store, column-based store (like BigTable, Cassandra, Hypertable)
    - used in Facebook messenger

# Comparisions and practices
- In-memory engines:
  - Faster than on-disk engines
  - Pandas is most widely supported but slower than other options
    - Pandas 2.0 integrates pyArrow for better performance to close the gap but still slower
  - Different solutions to Pandas slowness:
    - Pandas 2.0 - integrates pyArrow for better performance
    - Polars - rewrite Pandas from scratch with parallelism in mind
    - DuckDB - separate project, wraps a data source and performs large analytics with parallelism
    - Dask - user-controled paritions and dataframe per partition
  - According non-pandas options https://www.youtube.com/watch?v=DwtbPhbDecQ&t=535s
    - No option is consistently faster than the others
      - DuckDB comes the closest
      - At very high scale (>10TB in the cloud), dask, duckdb, and spark shoudl be considered.
- On-disk, single machine engines (SQL):
    - SQL wont have the memory constraints as with in-memory engines
    - SQL result may come slower (not accounting for time to load into memory) but can handle larger datasets
- Distributed, on-disk engines like Hadoop still have use cases, but fewer cases for data scientists workflows
- For big data analytics, Spark is usually the better option.
- OLAP--online analytical processing--(Apagche Druid, Kylin, Pinot) databases are an option for regular/similar business analytics queries
  - Reminder: Databases uses can be large analytical queries, or small fast record keeping, among others
  - OLAP is an analytical processing more for business analytics, closer to datascience
  - OLTP is another paradigm that has more to do with transactional processing of individual records and ACID
    - ACID: Atomicity, Consistency, Isolation, Durability - part of SQL that is sacraficed in NoSQL
      - See Turing Award winner, Michael Stonebraker's talks on Youtube for an explanation and contraversal take

