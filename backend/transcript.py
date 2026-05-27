from youtube_transcript_api import YouTubeTranscriptApi
def extract_video_id(youtube_url):

    if "v=" in youtube_url:
        return youtube_url.split("v=")[1]

    return None

def get_transcript(video_id):

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    return transcript

def transcript_to_text(transcript_data):

    full_text = ""

    for entry in transcript_data:
        full_text += entry.text + " "

    return full_text

