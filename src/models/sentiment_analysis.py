from pydantic import BaseModel, UUID4

class SentimentAnalysis(BaseModel):
    document_text: str
    polarity_score: float
    subjectivity_score: float
    n_gram: int
    text_id: UUID4

