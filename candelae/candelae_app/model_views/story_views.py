from django.http import JsonResponse


def get_all_stories(request):
    json_dict = {"stories": "all"}
    return JsonResponse(json_dict)


def get_story(request):
    json_dict = {"stories": "concrete"}
    return JsonResponse(json_dict)


def add_story(request):
    json_dict = {"stories": "add"}
    return JsonResponse(json_dict)
