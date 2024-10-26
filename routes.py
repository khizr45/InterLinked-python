from flask import Flask, jsonify, request
from flask_cors import CORS
import cv_to_json as cv_to_json

app = Flask(__name__)

CORS(app)

@app.route('/api/cv-to-json', methods=['POST'])
def cvToJson():
    if 'file' not in request.files:
        return jsonify({'message': 'File not found'}), 400

    file = request.files['file']

    if file and file.filename.endswith('.pdf'):
        response_json = cv_to_json.cv_to_json(file)
        return jsonify(response_json), 200

    return jsonify({'message': 'Invalid file type, please upload a PDF'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)