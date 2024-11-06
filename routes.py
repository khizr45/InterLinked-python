from flask import Flask, jsonify, request
from flask_cors import CORS
import cv_to_json as cv_to_json
import cv_ranking as cv_ranking

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


@app.route('/api/cv-ranking',methods=['POST'])
def cvRanking():
    data = request.get_json()
    if 'job_json' not in data:
        return jsonify({'message' : "job json not found"}),400
    if 'candidate_json' not in data:
        return jsonify({'message' : "candidate json not found"}),400
    job_json = data['job_json']
    candidate_json = data['candidate_json']
    overall_similarity,title_similarity,skills_similarity,experience_similarity,domain_similarity = cv_ranking.cvRanking(job_json,candidate_json)
    if overall_similarity and title_similarity and skills_similarity and experience_similarity and domain_similarity:
        return jsonify({'rank' : overall_similarity , 
                        'title' : title_similarity,
                        'skills' : skills_similarity,
                        'description' : experience_similarity,
                        'domain' : domain_similarity}),200
    return jsonify({'message' : "server error"}),500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)