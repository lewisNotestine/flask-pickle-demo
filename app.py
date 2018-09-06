#!flask/bin/python
from flask import Flask, request
from model import Model
import json
import os

app_path = os.path.dirname(os.path.realpath(__file__))
model_path = f"{app_path}/pickles/model.p"
model = Model(model_path)

app = Flask(__name__)

@app.route('/')
def index():
    """Health check."""
    return "Healthy!"

@app.route('/model', methods=['POST'])
def apply_model():
    data = json.loads(request.data)
    model_result = model.apply_model(data)
    output = list(map(lambda x: x[0], model_result))

    return json.dumps(output)

if __name__ == '__main__':
    app.run(debug=True)