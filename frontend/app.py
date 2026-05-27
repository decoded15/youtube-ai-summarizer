import streamlit as st
import requests

st.title("🎥 AI YouTube Video Summarizer")

youtube_url = st.text_input("Enter YouTube URL")

summarize_button = st.button("Generate Summary")

if summarize_button:

    with st.spinner("Summarizing video..."):

        response = requests.post(

            "http://127.0.0.1:8000/summarize",

            json={
                "youtube_url": youtube_url
            }
        )

        data = response.json()

    if "summary" in data:
        st.subheader("Summary")
        st.write(data["summary"])

    else:
        st.error(data["detail"])