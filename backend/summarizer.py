import google.generativeai as genai

from config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def create_chunks(text, chunk_size=3000):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks

def summarize_chunks(chunks):

    chunk_summaries = []

    for chunk in chunks:

        prompt = f"""
        Summarize the following transcript section.

        Transcript:
        {chunk}
        """

        response = model.generate_content(prompt)

        chunk_summaries.append(response.text)

    return chunk_summaries

def combine_summaries(chunk_summaries):

    combined_text = "\n".join(chunk_summaries)

    final_prompt = f"""
    Combine the following partial summaries
    into one complete final summary.

    Summaries:
    {combined_text}
    """

    response = model.generate_content(final_prompt)

    return response.text

def generate_summary(transcript_text):

    chunks = create_chunks(transcript_text)

    chunk_summaries = summarize_chunks(chunks)

    final_summary = combine_summaries(chunk_summaries)

    return final_summary