from flask import Flask, jsonify, request
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def generate_token():
    try:
        client_id = request.form.get("client_id")
        client_secret_key = request.form.get("client_secret_key")
        print(client_id,client_secret_key)

        env_client_id = os.getenv("CLIENT_ID")
        env_client_secret = os.getenv("CLIENT_SECRET")
        print(env_client_id)
        print(env_client_secret)

        if client_id != env_client_id or client_secret_key != env_client_secret:
            return jsonify({"responseCode": 401, "message": "Client information not valid"})

        # Generate JWT token
        payload = {
            'client_id': client_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
        }
        token = jwt.encode(payload, client_secret_key, algorithm='HS256')

        return jsonify({"responseCode": 200, "message": "Token generated successfully", "token": token})

    except Exception as e:
        return jsonify({"Error": str(e)})