import flask
from flask import request, jsonify
from sentence_transformers import SentenceTransformer
import json

app = flask.Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

@app.route("/checking", methods=["GET"])
def checking():
    return "Working!!"

@app.route("/preprocess", methods=["POST"])
def preprocess_text():
    data = request.get_json()
    texts = [data.get()]
    print(texts)
    print("-----------------------")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    print(embeddings)
    return jsonify({"message": "processed successfully"})

def convert_json_to_text(data):
    texts = []
    for item in data:
        text = item.get("text")
        texts.append(text)
    return texts

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Change port if needed
