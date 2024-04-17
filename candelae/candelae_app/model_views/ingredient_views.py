from django.http import JsonResponse


def get_all_ingredients(request):
    json_dict = {"ingredients": "all"}
    return JsonResponse(json_dict)


def get_ingredient(request):
    json_dict = {"ingredients": "concrete"}
    return JsonResponse(json_dict)


def add_ingredient(request):
    json_dict = {"ingredients": "add"}
    return JsonResponse(json_dict)
