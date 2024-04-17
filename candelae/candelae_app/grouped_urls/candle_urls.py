from django.urls import path
from ..model_views import candle_views


urlpatterns = [
    path("candles/search/", candle_views.get_all_candles, name="candles")
]