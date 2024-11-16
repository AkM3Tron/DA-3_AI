from llama_index import GPTSimpleVectorIndex
from flask import Flask, request, jsonify

app = Flask(__name__)
index = GPTSimpleVectorIndex.load_from_disk('technical_index.json')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('question', '')
    response = index.query(question)
    return jsonify({"response": str(response)})

if __name__ == '__main__':
    app.run(port=5000)
