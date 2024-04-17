from django.urls import path
from ..model_views import storytype_views


urlpatterns = [
    path("story_types", storytype_views.get_all_story_types, name="story_types"),
]