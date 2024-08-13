# unified_api_server.py
from mongoengine import connect
import yaml
with open("secret.yml", "r") as file:
    config = yaml.safe_load(file)
MongoURI = config["MONGO_URI"]
# Define the MongoDB connection settings
MONGODB_SETTINGS = {"db": "StockInfoDB", "host": MongoURI}
# Connect to the MongoDB database using the connection settings
connect(**MONGODB_SETTINGS)

from flask import Flask, request, jsonify
from flask_cors import CORS
from query_router import route_query
from graphql_api import graphql_api
from rest_api import rest_api

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(rest_api, url_prefix="/api")
app.register_blueprint(graphql_api)

# Bot endpoint
@app.route('/bot', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    try:
        response = route_query(query)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)


