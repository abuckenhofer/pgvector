# pg_vector
Example usage for PostgreSQL VectorDB extension.

## Prerequisites 
Python must be installed.

A PostgreSQL database with installed pg_vector exists. Follow [installation description](https://github.com/pgvector/pgvector) or use a pgvector-ready docker container, e.g.

docker run -d -e POSTGRES_PASSWORD=... --name pgvector pgvector/pgvector:pg16

docker exec -it pgvector bash

## Steps to run example
- install the required Python packages with "pip install -r requirements.txt"
- run the sql Skript 01_createTabs.sql in PostgreSQL zu create the tables
- check .env for your PostgreSQL environment and set password
- run the Python script 02_embeddings.py to create the embeddings
- query the PostgreSQL tables with similarity search

