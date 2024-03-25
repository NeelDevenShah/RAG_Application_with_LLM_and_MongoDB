import flask
from flask import request, jsonify
from sentence_transformers import SentenceTransformer
import json
import socketserver
import threading

app = flask.Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

@app.route("/checking", methods=["GET"])
def checking():
    return "Working!!"

@app.route("/preprocess", methods=["POST"])
def preprocess_text():
    data = request.get_json()
    texts = []
    for key, value in data.items():
        texts.append(f"{key}: {value}")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    print("Processed a request successfully")
    return jsonify({"embeddings": embeddings.tolist()})

def convert_json_to_text(data):
    texts = []
    for item in data:
        text = item.get("text")
        texts.append(text)
    return texts

if __name__ == "__main__":
    server = ThreadedTCPServer(('0.0.0.0', 5000), app)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server started.")
    server_thread.join()
