from flask import Flask, jsonify

app = Flask(__name__)

# Sample API endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"}), 200

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
