from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pyngrok import ngrok
from flask_cors import CORS

load_dotenv()  # Load environment variables from .env file
ngrok_auth_token = os.getenv("NGROK_AUTH_TOKEN")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Home page route
@app.route('/api/home', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!"})

# Root page route
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"message": data['message']}), 200

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))


    ngrok.set_auth_token(ngrok_auth_token)
    public_url = ngrok.connect(port)
    print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")
    
    app.run(port=port)