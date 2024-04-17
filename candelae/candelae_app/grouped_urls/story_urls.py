from django.urls import path
from ..model_views import story_views


urlpatterns = [
    path("stories", story_views.get_all_stories, name="stories"),
]