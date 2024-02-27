from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.test_db
clients_collection = db.test_clients

def insert_initial_client():
    db.test_clients.insert_one({"client_id": "test-api", "client_secret_key": "6a1a65e6-cf21-4b45-a749-04c31cc1fdf9"})

insert_initial_client()