from django.urls import path
from ..model_views import storytype_views


urlpatterns = [
    path("search/", storytype_views.get_story_types_contains_name, name="story_types"),
    path("", storytype_views.get_all_story_types, name="story_types"),
    path("create/", storytype_views.create_story_type, name="story_types")
]