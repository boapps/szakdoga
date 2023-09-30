from flask import Flask, request, jsonify
import random
from transformers import BertForSequenceClassification, BertTokenizer
import torch
import torch.nn.functional as F

model = BertForSequenceClassification.from_pretrained('boapps/kmdb_classification_model')
tokenizer = BertTokenizer.from_pretrained('SZTAKI-HLT/hubert-base-cc')

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def index():
    data = request.get_json()
    inputs = tokenizer(data['text'], return_tensors="pt")
    logits = model(**inputs).logits
    probabilities = F.softmax(logits[0], dim=-1)
    res = torch.argmax(logits, axis=1)[0]
    corruption = probabilities[0] < 0.42
    return jsonify({"class": "corruption" if corruption else "other"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)