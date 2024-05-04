from django.urls import path
from ..model_views import ingredient_views


urlpatterns = [
    path("search/", ingredient_views.get_ingredients_contains_name, name="ingredients"),
    path("", ingredient_views.get_all_ingredients, name="ingredients"),
    path("create/", ingredient_views.create_ingredient, name="ingredients")
]