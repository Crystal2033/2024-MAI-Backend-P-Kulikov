from django.urls import path
from ..model_views import candle_views


urlpatterns = [
    path("search/", candle_views.get_candles_contains_name_or_description_or_story, name="candles_search"),
    path("", candle_views.get_all_candles, name="candles"),
    path("create/", candle_views.create_candle, name="candles")
]