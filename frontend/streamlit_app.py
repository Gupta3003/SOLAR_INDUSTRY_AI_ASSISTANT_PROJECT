import streamlit as st
import requests

st.title("Solar Rooftop Analysis Assistant")

uploaded_file = st.file_uploader("Upload a rooftop image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    if st.button("Analyze Rooftop"):
        files = {'image': uploaded_file.getvalue()}
        response = requests.post("http://localhost:5000/analyze", files=files)
        if response.status_code == 200:
            result = response.json()
            st.success("Analysis Completed")
            st.json(result)
        else:
            st.error("Error analyzing image")
