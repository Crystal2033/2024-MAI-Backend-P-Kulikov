from django.urls import path
from . import views
from .model_views import candle_views

urlpatterns = [
    path("", views.home, name="home"),
    path("candles", candle_views.get_all_candles, name="candles")
]