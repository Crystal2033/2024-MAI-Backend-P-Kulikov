from django.urls import path
from ..model_views import ingredient_views


urlpatterns = [
    path("ingredients", ingredient_views.get_all_ingredients, name="ingredients")
]