from django.urls import path
from ..model_views import storytype_views


urlpatterns = [
    path("story_types/search/", storytype_views.get_story_types_contains_name, name="story_types"),
    path("story_types/", storytype_views.get_all_story_types, name="story_types"),
]