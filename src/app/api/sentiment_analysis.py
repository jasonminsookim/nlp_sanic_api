from starlite import Controller, Partial, get, post, put, patch, delete

from app.models.sentiment_analysis import SentimentAnalysis

class SentimentAnalysisController(Controller):
    path = "/sentiment_analysis"

    @post()
    async def analyze_sentiment(self, data:SentimentAnalysis) -> SentimentAnalysis:
        return SentimentAnalysis(document_text="hello")
    

