from fastapi import FastAPI
from pydantic import BaseModel
from transcript import (
    extract_video_id,
    get_transcript,
    transcript_to_text
)

app = FastAPI()


class VideoRequest(BaseModel):
    youtube_url: str


@app.post("/summarize")
def summarize_video(data: VideoRequest):

    video_id = extract_video_id(data.youtube_url)

    transcript_data = get_transcript(video_id)

    transcript_text = transcript_to_text(transcript_data)

    return {
        "video_id": video_id,
        "transcript": transcript_text
    }