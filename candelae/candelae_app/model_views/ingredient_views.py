from django.http import JsonResponse

from ..my_models.Ingredient import Ingredient
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON
from ..exceptions.DataNotFound import DataNotFoundException
from ..exceptions.InputDataError import InputDataException


def get_all_ingredients(request):
    ingredients = Ingredient.objects.all()
    return JsonResponse({"ingredients": FromQuerySetToJSON.convert(ingredients)})


def get_ingredients_contains_name(request):
    searching_str = request.GET.get('q')
    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    ingredients_request = (Ingredient.objects
                           .filter(name__icontains=searching_str)
                           .all())
    ingredients = FromQuerySetToJSON.convert(ingredients_request)
    return JsonResponse({"ingredients": ingredients})


def get_ingredient(request):
    json_dict = {"ingredients": "concrete"}
    return JsonResponse(json_dict)


def add_ingredient(request):
    json_dict = {"ingredients": "add"}
    return JsonResponse(json_dict)
