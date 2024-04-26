import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..exceptions.InputDataError import InputDataException
from ..my_models.Ingredient import Ingredient
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON
from ..exceptions.NotCompatibleRequestException import NotCompatibleRequestException


def get_all_ingredients(request):
    if request.method == "GET":
        print("GET")
        ingredients = Ingredient.objects.all()
        return JsonResponse({"ingredients": FromQuerySetToJSON.convert(ingredients)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


@csrf_exempt
def create_ingredient(request):
    if request.method == "POST":
        print("POST")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        ingredient = Ingredient(**body)
        ingredient.save()
        return JsonResponse({"ingredient": model_to_dict(ingredient)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


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
