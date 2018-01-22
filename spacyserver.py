from spacy.en import English
from flask import Flask, request, jsonify

app = Flask(__name__)

nlp = English()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/parse')
def parse():
    text = request.args.get('text')
    doc = nlp(text)
    return jsonify(doc=doc)

if __name__ == '__main__':
    app.run(debug=True)
