# pgvector
Example usage for PostgreSQL VectorDB extension.

## Prerequisites 
A PostgreSQL database with installed pg_vector exists. Follow [installation description](https://github.com/pgvector/pgvector) or use a ready docker container, e.g.

docker run -d -e POSTGRES_PASSWORD=... --name pgvector pgvector/pgvector:pg16

docker exec -it pgvector bash

Python must be installed.

## Steps to run example
- install the required Python packages with pip install requirements.txt
- run the sql Skript in PostgreSQL zu create the tables
- run the Python script to create the embeddings
- query the PostgreSQL tables with similarity search

