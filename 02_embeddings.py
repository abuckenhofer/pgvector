import torch
from transformers import BertTokenizer, BertModel
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv
import os

load_dotenv()

# Generierung von Embeddings mit BERT
def generate_embedding(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Verwenden des Durchschnitts der letzten versteckten Zustände als Embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding.tolist()
    
# Verbindung zur PostgreSQL-Datenbank
conn = psycopg2.connect(
    dbname=os.environ["PG_DBNAME"], 
    user=os.environ["PG_USER"], 
    password=os.environ["PG_PASSWORD"], 
    host=os.environ["PG_HOST"], 
    port=os.environ["PG_PORT"]
)
cursor = conn.cursor()

# Testdaten
user_preferences = ["Oracle Vector DB", 
                    "PostgreSQL"]
item_properties = ["Wrap up your PostgreSQL environment with TPA", 
                   "Enabling Generative-AI with Oracle AI Vector Search", 
                   "Oracle DBMS meets Generative AI: from Text-to-SQL to Vector DB",
                   "Is PostgreSQL catching up with the Oracle Database?"
                   ]

# Generieren von Embeddings für Besucherpräferenzen und Titeleigenschaften
user_embeddings = [generate_embedding(text) for text in user_preferences]
item_embeddings = [generate_embedding(text) for text in item_properties]

# Einfügen von Embeddings in die Datenbank
user_insert_query = "INSERT INTO vector.visitor (preferences) VALUES (%s)"
item_insert_query = "INSERT INTO vector.topic (properties) VALUES (%s)"

execute_batch(cursor, user_insert_query, [(embedding,) for embedding in user_embeddings])
execute_batch(cursor, item_insert_query, [(embedding,) for embedding in item_embeddings])

# Commit und Aufräumen
conn.commit()
cursor.close()
conn.close()

print("Embeddings erfolgreich eingefügt.")
