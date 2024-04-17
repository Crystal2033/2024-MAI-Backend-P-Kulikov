from django.db.models import Q
from django.http import JsonResponse
from ..my_models.Story import Story
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON
from ..exceptions.DataNotFound import DataNotFoundException
from ..exceptions.InputDataError import InputDataException

def get_all_stories(request):
    json_dict = {"stories": "all"}
    return JsonResponse(json_dict)


def get_stories_contains_short_name_or_description(request):
    searching_str = request.GET.get('q')
    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    stories_request = (Story.objects
                       .filter(Q(short_story_name__contains=searching_str) | Q(description__contains=searching_str))
                       .all())
    stories = FromQuerySetToJSON.convert(stories_request)
    return JsonResponse({"stories": stories})


def get_story(request):
    json_dict = {"stories": "concrete"}
    return JsonResponse(json_dict)


def add_story(request):
    json_dict = {"stories": "add"}
    return JsonResponse(json_dict)
