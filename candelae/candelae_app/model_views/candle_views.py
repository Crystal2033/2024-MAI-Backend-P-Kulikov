from django.db.models import Q
from django.http import JsonResponse
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON
from ..my_models.Candle import Candle
from ..exceptions.DataNotFound import DataNotFoundException
from ..exceptions.InputDataError import InputDataException


def get_all_candles(request):
    json_dict = {"candles": request.GET.get('q')}
    return JsonResponse(json_dict)


def get_candles_contains_name_or_description_or_story(request):
    searching_str = request.GET.get('q')
    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    candles_request = (Candle.objects
                       .filter(Q(name__contains=searching_str) | Q(description__contains=searching_str))
                       .all())
    candles = FromQuerySetToJSON.convert(candles_request)
    return JsonResponse({"candles": candles})


def get_candle(request):
    json_dict = {"candles": "concrete"}
    return JsonResponse(json_dict)


def add_candle(request):
    json_dict = {"candles": "add"}
    return JsonResponse(json_dict)
