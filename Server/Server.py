from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask server!'})


@app.route('/api/data', methods=['GET'])
def get_data():
    # Perform any necessary operations or retrieve data from a database
    data = {'data': [1, 2, 3, 4, 5]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
