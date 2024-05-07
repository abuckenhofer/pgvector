# pg_vector
Example usage for PostgreSQL VectorDB extension.

## Prerequisites 
Python must be installed.

A PostgreSQL database with installed pg_vector exists. Follow [installation description](https://github.com/pgvector/pgvector) or use a pgvector-ready docker container, e.g.

docker run -d -e POSTGRES_PASSWORD=... --name pgvector pgvector/pgvector:pg16

docker exec -it pgvector bash

Now the PostgreSQL command shell can be started: psql -U postgres 

## Steps to run example
- install the required Python packages with "pip install -r requirements.txt"
- run the sql Skript 01_createTabs.sql in PostgreSQL to create the tables
- check .env for your PostgreSQL environment and set password
- run the Python script 02_embeddings.py to create the embeddings
- query the PostgreSQL tables with similarity search. Example queries can be found at the end of the script in 01_createTabs.sql

For more information on Vector databases see my personal blog, e.g. [Vector databases - what, why, and how](https://buckenhofer.com/2024/05/vector-database-what-why-and-how/).

