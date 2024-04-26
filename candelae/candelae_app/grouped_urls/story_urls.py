from django.urls import path
from ..model_views import story_views


urlpatterns = [
    path("stories/", story_views.get_all_stories, name="stories"),
    path("stories/search/", story_views.get_stories_contains_short_name_or_description, name="stories"),
    path("stories/create/", story_views.create_story, name="stories")

]