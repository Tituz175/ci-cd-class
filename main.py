from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Hello, CS24")

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'result': a + b})

@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'result': a - b})

@app.route('/div', methods=['GET'])
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'result': a / b})

@app.route('/mul', methods=['GET'])
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'result': a * b})

@app.route('/pow', methods=['GET'])
def pow():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return jsonify({'result': a ** b})


if __name__ == "__main__":
    app.run(debug=True)