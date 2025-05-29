from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    # Mocked analysis result
    result = {
        "rooftop_area": "65 sqm",
        "estimated_output": "8.5 kW",
        "roi": "4.2 years",
        "recommendation": "Optimal for 20-panel setup"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
