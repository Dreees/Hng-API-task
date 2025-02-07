from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return "The Famous Number API!"

if __name__ == '__main__':
    app.run(debug=True)