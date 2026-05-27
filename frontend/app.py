import streamlit as st
import requests

st.title("🎥 AI YouTube Video Summarizer")

st.caption(
    "Paste a YouTube video link to get an AI-generated summary instantly."
)

youtube_url = st.text_input("Enter YouTube URL")

summary_mode = st.selectbox(

    "Select Summary Type",

    [
        "Short Summary",
        "Detailed Notes",
        "Bullet Points",
        "Beginner Friendly"
    ]
)

summarize_button = st.button("Generate Summary")

if summarize_button:

    if not youtube_url:

        st.warning("Please enter a YouTube URL.")

    elif "youtube.com" not in youtube_url and "youtu.be" not in youtube_url:

        st.error("Please enter a valid YouTube URL.")

    else:
        try:
            with st.spinner("Summarizing video..."):

                response = requests.post(

                    "http://127.0.0.1:8000/summarize",

                    json={
                        "youtube_url": youtube_url,
                        "summary_mode": summary_mode
                    }   
                )

                data = response.json()

            if "summary" in data:
                st.subheader("Videp Summary")
                with st.container():
                    st.markdown(data["summary"])

            else:
                st.error(f"Error: {data['detail']}")

        except requests.exceptions.ConnectionError:

            st.error("Backend server is not running.")