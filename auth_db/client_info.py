from auth_db.db_setup import clients_collection

def get_client_info(client_id):
    return clients_collection.find_one({"client_id": client_id})
