from flask import Flask, jsonify
from auth.token_required import token_required
from auth.generate_token import generate_token

app = Flask(__name__)


@app.route('/generate_token', methods=['POST'])
def get_token():
    return generate_token()

@app.route('/protected_route', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'This is a protected route!'})

if __name__ == '__main__':
    app.run(debug=True)
