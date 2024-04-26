import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..exceptions.InputDataError import InputDataException
from ..exceptions.NotCompatibleRequestException import NotCompatibleRequestException
from ..my_models.StoryType import StoryType
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON


def get_all_story_types(request):
    if request.method == "GET":
        print("GET")
        story_types = StoryType.objects.all()
        return JsonResponse({"story_types": FromQuerySetToJSON.convert(story_types)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


@csrf_exempt
def create_story_type(request):
    if request.method == "POST":
        print("POST")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        story_type = StoryType(**body)
        story_type.save()
        return JsonResponse({"story_type": model_to_dict(story_type)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)

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
