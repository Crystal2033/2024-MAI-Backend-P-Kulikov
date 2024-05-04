from django.urls import path
from ..model_views import story_views


urlpatterns = [
    path("", story_views.get_all_stories, name="stories"),
    path("search/", story_views.get_stories_contains_short_name_or_description, name="stories"),
    path("create/", story_views.create_story, name="stories")

]