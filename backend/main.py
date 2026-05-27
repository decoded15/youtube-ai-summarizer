from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class VideoRequest(BaseModel):
    youtube_url: str


@app.post("/summarize")
def summarize_video(data: VideoRequest):

    return {
        "message": "Request received successfully",
        "youtube_url": data.youtube_url
    }