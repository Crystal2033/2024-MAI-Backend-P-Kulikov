from django.http import JsonResponse


def get_all_story_types(request):
    json_dict = {"story_types": "all"}
    return JsonResponse(json_dict)


def get_story_type(request):
    json_dict = {"story_types": "concrete"}
    return JsonResponse(json_dict)


def add_story_type(request):
    json_dict = {"story_types": "add"}
    return JsonResponse(json_dict)
