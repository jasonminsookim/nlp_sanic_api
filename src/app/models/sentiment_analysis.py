from pydantic import BaseModel


class SentimentAnalysis(BaseModel):
    document_text: str
