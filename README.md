
# ☀️ Solar Industry AI Assistant

An AI-powered rooftop analysis tool that uses satellite imagery and OpenRouter's Vision AI to assess the potential for solar panel installation. This system is designed to assist homeowners and solar professionals by providing insights such as installation feasibility and ROI estimates.

---

## 🎯 Project Goal

- Analyze rooftop images using Vision AI
- Assess solar potential and provide ROI estimations
- Deliver structured recommendations using AI-driven analysis
- Build a modular tool with a Flask backend and Streamlit frontend

---

## 🧠 Key Features

- 🔍 Upload and analyze rooftop images
- 🤖 Vision AI (via OpenRouter) for rooftop understanding
- 💡 Suggest installation capacity and payback time
- 📈 ROI and solar area estimation
- 🖥️ Web-based interface via Streamlit
- 🛠️ Modular backend built using Flask

---

## 🛠 Tech Stack

| Component  | Technology                    |
|------------|-------------------------------|
| AI Model   | OpenRouter Vision (GPT-4V, Claude 3 Opus) |
| Backend    | Flask (Python)                |
| Frontend   | Streamlit                     |
| Hosting    | Localhost (for now)           |
| Data Format| Image Upload (JPEG/PNG)       |

---

## 📁 Project Structure

```
solar_industry_ai_assistant/
├── backend/             # Flask API
│   └── app.py
├── frontend/            # Streamlit UI
│   └── streamlit_app.py
├── requirements.txt     # Python dependencies
├── README.md            # You're reading it!
├── requirements.txt     # requriments. txt file
├── .gitignore           # contain enviroment varible and .env OpenRouter API key holder
```

---

## ⚙️ Setup Instructions (Local)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Your API Key
Create a file named `.env` in the project root with:
```
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx
```

Or hardcode the key in `backend/app.py` temporarily (not recommended for production).

### 3. Run Backend (Flask API)
```bash
cd backend
python app.py
```

### 4. Run Frontend (Streamlit)
In a separate terminal:
```bash
cd frontend
streamlit run streamlit_app.py
```

---

## Frontend Interface

### Screenshots

| Solar Rooftop Analysis Assistant     | Result Analysis                                                                                                                             |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|![Image](https://github.com/user-attachments/assets/a5b24bbe-1215-4e83-8a0a-1bce1ac67b20)| ![Image](https://github.com/user-attachments/assets/375c3591-ab40-4d4e-93b0-2d3e8d377cba)|


### Demo Vedio
https://github.com/user-attachments/assets/9f82cf33-8c60-4b2b-8060-37da75c04312

## 🧪 Example Use Case

1. Open the Streamlit app in your browser.
2. Upload a rooftop image (e.g., from Google Maps).
3. Click "Analyze Solar Potential".
4. View Vision AI results and estimated ROI suggestions.

---

## 📌 Notes

- This is a **local project**. No deployment has been done yet.
- Uses **OpenRouter Vision API** for AI analysis.
- All results are mock ROI estimates for demonstration purposes.
- Make sure to stay within your OpenRouter API usage limits.

---

## 🔮 Future Improvements

- Add image pre-processing for better rooftop detection
- Deploy on Hugging Face Spaces or Render
- Integrate real-world ROI formulas based on location & panel specs
- Add PDF report download feature
- Implement login/auth system for multiple users

---
