CREATE EXTENSION IF NOT EXISTS vector;

DROP SCHEMA if exists vector CASCADE;
CREATE SCHEMA vector;

-- Tabelle für Besucher mit ihren Präferenz-Vektoren
CREATE TABLE vector.visitor (
    user_id SERIAL PRIMARY KEY,
    preferences VECTOR(768) 
);

-- Tabelle für Vortragstitel mit ihren Eigenschafts-Vektoren
CREATE TABLE vector.topic (
    item_id SERIAL PRIMARY KEY,
    properties VECTOR(768) 
);

-- Beispiele für Vektor-Indexe
--CREATE INDEX user_embeddings_embedding_idx ON vector.visitor USING hnsw (preferences vector_l2_ops);
--CREATE INDEX item_embeddings_embedding_idx ON vector.topic USING hnsw (properties vector_l2_ops);

/*
-- Beispielabfragen wenn Tabellen gefuellt sind
SELECT item_id, properties <-> (SELECT preferences FROM vector.visitor WHERE user_id = 1) AS similarity
FROM vector.topic
ORDER BY similarity
LIMIT 10;

SELECT item_id, properties <-> (SELECT preferences FROM vector.visitor WHERE user_id = 2) AS similarity
FROM vector.topic
ORDER BY similarity
LIMIT 10;
*/

