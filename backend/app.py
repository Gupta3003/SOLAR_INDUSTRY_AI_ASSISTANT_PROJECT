from flask import Flask, request, jsonify
import requests
import os
import base64
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
VISION_API_URL = "https://openrouter.ai/api/v1/chat/completions"

if OPENROUTER_API_KEY:
    print("OPENROUTER_API_KEY is set.")
else:
    print("WARNING: OPENROUTER_API_KEY environment variable is NOT set. API calls will likely fail.")

def analyze_image_with_openrouter(image_bytes):
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    print(f"DEBUG: Using API Key (first 10 chars): {OPENROUTER_API_KEY[:10] if OPENROUTER_API_KEY else 'NONE'}")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o",  # ✅ Correct model name for OpenRouter
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image and provide a detailed description of its contents, focusing on any structures, objects, or features that could be relevant for estimating solar panel suitability, such as roof type, shading, available area, and surrounding environment."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }

    print(f"Sending request to: {VISION_API_URL}")
    try:
        response = requests.post(VISION_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()

        try:
            return response.json()
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            print(f"Raw response content: {response.text}")
            raise ValueError(f"Failed to decode JSON from OpenRouter API. Raw response: {response.text[:500]}...")
    except requests.exceptions.RequestException as e:
        print(f"Request to OpenRouter API failed: {e}")
        if e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        raise

@app.route("/analyze", methods=["POST"])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()

    try:
        analysis_result = analyze_image_with_openrouter(image_bytes)

        model_output = "No analysis text found."
        if analysis_result and 'choices' in analysis_result and analysis_result['choices']:
            for choice in analysis_result['choices']:
                if 'message' in choice and 'content' in choice['message']:
                    model_output = choice['message']['content']
                    break

        roi_estimate = {
            "suitable_area": "35 sqm",
            "recommended_capacity": "5 kW",
            "estimated_roi": "7 years",
            "confidence": "High"
        }

        return jsonify({
            "analysis_result": model_output,
            "full_api_response": analysis_result,
            "roi_estimate": roi_estimate
        })
    except Exception as e:
        print(f"An error occurred in /analyze endpoint: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
