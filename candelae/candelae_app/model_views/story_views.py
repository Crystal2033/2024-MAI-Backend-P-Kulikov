import json

from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..exceptions.InputDataError import InputDataException
from ..my_models.Story import Story
from ..my_models.StoryType import StoryType
from ..util.ArrayToJSONSerializer import FromQuerySetToJSON


def get_all_stories(request):
    if request.method == "GET":
        print("GET")
        stories = Story.objects.all()
        return JsonResponse({"stories": FromQuerySetToJSON.convert(stories)})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


@csrf_exempt
def create_story(request):
    if request.method == "POST":
        print("POST")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        story_types = []
        set_of_types = set()
        for story_type_id in body["story_types"]:
            if set_of_types.__contains__(story_type_id):
                return JsonResponse({"error": 400, "message": "Duplicate object"}, status=400)
            set_of_types.add(story_type_id)
            story_type = StoryType.objects.get(pk=story_type_id)
            story_types.append(story_type)

        story = Story.objects.create(short_story_name=body["short_story_name"], description=body["description"])
        story.story_types.set(story_types)

        list_of_story_types = story.story_types.all()
        story_dict = model_to_dict(story)
        story_dict["story_types"] = FromQuerySetToJSON.convert(list_of_story_types)

        return JsonResponse({"story": story_dict})
    else:
        return JsonResponse({"error": 400, "message": "Unknown request method for current path"}, status=400)


def get_stories_contains_short_name_or_description(request):
    searching_str = request.GET.get('q')
    if searching_str is None or len(searching_str) == 0:
        raise InputDataException("Your query string can not be empty")

    stories_request = (Story.objects
                       .filter(Q(short_story_name__icontains=searching_str) | Q(description__icontains=searching_str))
                       .all())
    stories = FromQuerySetToJSON.convert(stories_request)
    return JsonResponse({"stories": stories})


def get_story(request):
    json_dict = {"stories": "concrete"}
    return JsonResponse(json_dict)


def add_story(request):
    json_dict = {"stories": "add"}
    return JsonResponse(json_dict)
