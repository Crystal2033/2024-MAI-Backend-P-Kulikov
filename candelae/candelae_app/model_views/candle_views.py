import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..exceptions.InputDataError import InputDataException
from ..exceptions.NotCompatibleRequestException import NotCompatibleRequestException
from ..my_models.Candle import Candle
from ..my_models.Ingredient import Ingredient
from ..my_models.Story import Story
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON


def get_all_candles(request):
    if request.method == "GET":
        print("GET")
        candles = Candle.objects.all()
        return JsonResponse({"candles": FromQuerySetToJSON.convert(candles)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


@csrf_exempt
def create_candle(request):
    if request.method == "POST":
        print("POST")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        try:
            corresponding_story = Story.objects.get(pk=body["story_id"])
        except ObjectDoesNotExist:
            return JsonResponse({"error": 404, "message": "Story object not found"}, status=404)

        ingredients = []
        set_of_ingredients = set()
        for ingredient_id in body["ingredients"]:
            if set_of_ingredients.__contains__(ingredient_id):
                return JsonResponse({"error": 400, "message": "Duplicate object"}, status=400)
            set_of_ingredients.add(ingredient_id)
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            ingredients.append(ingredient)

        candle = Candle.objects.create(name=body["name"], description=body["description"], story=corresponding_story)
        candle.ingredients.set(ingredients)

        list_of_ingredients = candle.ingredients.all()

        story_types = corresponding_story.story_types.all()

        candle_dict = model_to_dict(candle)
        candle_dict["ingredients"] = FromQuerySetToJSON.convert(list_of_ingredients)

        story_dict = model_to_dict(corresponding_story)
        story_dict["story_types"] = FromQuerySetToJSON.convert(story_types)

        candle_dict["story"] = story_dict

        return JsonResponse({"candle": candle_dict})

    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


def get_candles_contains_name_or_description_or_story(request):
    searching_str = request.GET.get('q')
    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    candles_request = (Candle.objects
                       .filter(Q(name__icontains=searching_str) | Q(description__icontains=searching_str))
                       .all())
    candles = FromQuerySetToJSON.convert(candles_request)
    return JsonResponse({"candles": candles})


def get_candle(request):
    json_dict = {"candles": "concrete"}
    return JsonResponse(json_dict)


def add_candle(request):
    json_dict = {"candles": "add"}
    return JsonResponse(json_dict)
