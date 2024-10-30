from flask import Flask, request, jsonify
from math import factorial
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    n = data.get('n')
    r = data.get('r')

    if n < 0 or r < 0 or r > n:
        return jsonify({'error': 'Invalid input'}), 400

    p = permutations(n, r)
    c = combinations(n, r)

    return jsonify({'permutations': p, 'combinations': c})

if __name__ == '__main__':
    app.run(debug=True)
