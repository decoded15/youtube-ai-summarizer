import google.generativeai as genai

from config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def generate_summary(transcript_text):

    prompt = f"""
    Summarize the following YouTube video transcript.

    Include:
    - Main topic
    - Key points
    - Important insights

    Transcript:
    {transcript_text}
    """

    response = model.generate_content(prompt)

    return response.text