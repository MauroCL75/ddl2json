# ddl2json

This code will read DDL from a database user and generate a json string that will be displayed. It currently supports only Oracle database. The following objects are checked:
* Tables
* Columns on tables
* Indexes
You can later use the compare script to get the differences between two json files.

## Pre requisites
For Oracle you will need:
* Oracle's instant client
* cx_Oracle
You can also run ddl2json on the provided Dockerfile.

## Running this
You must follow this flow:
1. Run ./ddl2json.py "database connection1 string" > schema1.json
2. Run ./ddl2json.py "database connection1 string" > schema2.json
3. Run ./compare.py schema1.json schema2.json

## Docker
Create the container:
docker build -t cxoracle .
Run the container:
docker run -t cxoracle:latest ./venv/bin/python3 ddl2json.py "database connection1 string" > schema1.json

##About this
The ddl2json.py script get first the tables, then the columns and indexes for each table.
The queries are on the q.py file. DDL is retrieved for tables and indexes on the generated json file.

The compare.py script reads the tables, then compare the columns and indexes for each table. It will display DDL only for missing indexes.
