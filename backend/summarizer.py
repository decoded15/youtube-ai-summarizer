import google.generativeai as genai

from config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3.1-flash-lite")

def create_chunks(text, chunk_size=10000):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks

def summarize_chunks(chunks, summary_mode):

    chunk_summaries = []

    for chunk in chunks:

        prompt = get_prompt(chunk, summary_mode)

        response = model.generate_content(prompt)

        chunk_summaries.append(response.text)

    return chunk_summaries

def combine_summaries(chunk_summaries, summary_mode):

    combined_text = "\n".join(chunk_summaries)

    final_prompt = f"""
    Create a {summary_mode} style final summary
    from these partial summaries:

    {combined_text}
    """

    response = model.generate_content(final_prompt)

    return response.text


def get_prompt(transcript_text, summary_mode):

    if summary_mode == "Short Summary":

        return f"""
        Give a short concise summary
        of this YouTube transcript:

        {transcript_text}
        """

    elif summary_mode == "Detailed Notes":

        return f"""
        Create detailed notes from this
        YouTube transcript.

        Include:
        - main concepts
        - explanations
        - important insights

        Transcript:
        {transcript_text}
        """

    elif summary_mode == "Bullet Points":

        return f"""
        Summarize this transcript in bullet points.

        Transcript:
        {transcript_text}
        """

    elif summary_mode == "Beginner Friendly":

        return f"""
        Explain this transcript in very simple,
        beginner-friendly language.

        Transcript:
        {transcript_text}
        """
    else:
        return f"""Summarize this transcript:

        {transcript_text}
        """

def single_pass_summary(transcript_text, summary_mode):

    prompt = get_prompt(
        transcript_text,
        summary_mode
    )

    response = model.generate_content(prompt)

    return response.text

def generate_summary(transcript_text, summary_mode):

    if len(transcript_text) < 12000:
        return single_pass_summary(transcript_text, summary_mode)

    else:
        chunks = create_chunks(transcript_text)

        chunk_summaries = summarize_chunks(chunks, summary_mode)

        final_summary = combine_summaries(chunk_summaries, summary_mode)

        return final_summary
