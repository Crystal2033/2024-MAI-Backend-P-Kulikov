import json

from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..exceptions.InputDataError import InputDataException
from ..exceptions.NotCompatibleRequestException import NotCompatibleRequestException
from ..my_models.Candle import Candle
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
        candle = Candle(**body)
        candle.save()
        return JsonResponse({"ingredient": model_to_dict(candle)})
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
