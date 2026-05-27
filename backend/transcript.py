from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

def extract_video_id(youtube_url):

    if "v=" in youtube_url:
        return youtube_url.split("v=")[1]

    raise ValueError("Invalid YouTube URL")

def get_transcript(video_id):
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return transcript

    except NoTranscriptFound:
        raise ValueError(
            "Transcript not available for this video"
        )

def transcript_to_text(transcript_data):

    full_text = ""

    for entry in transcript_data:
        full_text += entry.text + " "

    return full_text

