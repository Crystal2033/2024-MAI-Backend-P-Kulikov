from django.http import JsonResponse

from ..my_models.Candle import Candle
from ..util.ArrayToJSONSerializer import ArrayToJSONSerializer, RecordType

def get_all_candles(request):
    # listOfCandles = [Candle(1, "Frodo", 1),
    #                  Candle(2, "Gendalf", 1),
    #                  Candle(3, "Legolas", 1),
    #                  Candle(4, "Elves forest", 1),
    #                  Candle(5, "Geralt", 2),
    #                  Candle(6, "Yennifer", 2),
    #                  Candle(7, "Cirilla", 2),
    #                  Candle(8, "Harry", 3),
    #                  Candle(9, "Germiona", 3),
    #                  Candle(10, "Ron", 3)]
    #
    # json_array_field_name = "candles"
    # json_dict = ArrayToJSONSerializer.get_dict_from_obj_list(listOfCandles, RecordType.CANDLE, json_array_field_name)
    json_dict = {}
    json_dict["test"] = 1
    return JsonResponse(json_dict)
