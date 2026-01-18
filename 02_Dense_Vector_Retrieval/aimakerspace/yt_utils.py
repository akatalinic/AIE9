from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import urllib.parse

class YTTranscriptLoader:
    def __init__(self, video_url: str):
        self.video_url = video_url
        self.documents = []

    def _extract_video_id(self) -> str:
        
        if "/" not in self.video_url and "?" not in self.video_url:
            return self.video_url

        url = urllib.parse.urlparse(self.video_url)

        if url.netloc == "youtu.be":
            video_id = url.path.lstrip("/")
            if video_id:
                return video_id

        if "youtube.com" in url.netloc:
            params = urllib.parse.parse_qs(url.query)
            video_id = params.get("v", [None])[0]
            if video_id:
                return video_id

        raise ValueError(f"Invalid YouTube URL or video ID: {self.video_url}")


    def load(self):
        self.documents = []
        video_id = self._extract_video_id()

        ytt = YouTubeTranscriptApi()

        try:
            transcript = ytt.fetch(video_id, languages=["en"])
        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video: {video_id}")
            return []
        except NoTranscriptFound:
            print(f"No English transcript found for video: {video_id}")
            return []
        except Exception as e:
            print(f"Error loading transcript: {e}")
            return []

        for item in transcript:
            text = item.text.strip()
            if text:
                self.documents.append(text)

        return self.documents

    def load_documents(self):
        return self.load()