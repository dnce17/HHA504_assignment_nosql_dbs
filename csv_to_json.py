import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

mongodb_password = os.getenv('mongodb_password')
uri = f'mongodb+srv://dnce17:{mongodb_password}@db-learning.rmy1k.mongodb.net/?retryWrites=true&w=majority&appName=db-learning'

df = pd.read_csv('patient_info.csv')
# Convert CSV to JSON-like format
data_dict_format = df.to_dict(orient='records')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Print list of colletions in the database
print(client.list_database_names())

# Access the healthcare database
healthcare_db = client['healthcare']

# Access a specific collection within that database
patient_info_collection = healthcare_db['patient_info']

# Insert the data into the MongoDB collection
patient_info_collection.insert_many(data_dict_format)