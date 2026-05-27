from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transcript import (
    extract_video_id,
    get_transcript,
    transcript_to_text
)
from summarizer import generate_summary

app = FastAPI()


class VideoRequest(BaseModel):
    youtube_url: str


@app.post("/summarize")
def summarize_video(data: VideoRequest):

    try:

        video_id = extract_video_id(data.youtube_url)

        transcript_data = get_transcript(video_id)

        transcript_text = transcript_to_text(transcript_data)

        summary = generate_summary(transcript_text)

        return {
            "video_id": video_id,
            "summary": summary
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )