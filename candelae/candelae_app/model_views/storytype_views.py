from django.http import JsonResponse

from ..my_models.StoryType import StoryType
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON
from ..exceptions.DataNotFound import DataNotFoundException
from ..exceptions.InputDataError import InputDataException


def get_all_story_types(request):
    story_types = StoryType.objects.all()
    return JsonResponse({"story_types": FromQuerySetToJSON.convert(story_types)})


def get_story_types_contains_name(request):
    searching_str = request.GET.get('q')

    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    story_types_request = (StoryType.objects
                           .filter(name__icontains=searching_str)
                           .all())
    story_types = FromQuerySetToJSON.convert(story_types_request)
    return JsonResponse({"story_types": story_types})


def get_story_type(request):
    json_dict = {"story_types": "concrete"}
    return JsonResponse(json_dict)


def add_story_type(request):
    json_dict = {"story_types": "add"}
    return JsonResponse(json_dict)
