from starlite import Starlite

from app import api

app = Starlite(route_handlers=[SentimentAnalysisController])