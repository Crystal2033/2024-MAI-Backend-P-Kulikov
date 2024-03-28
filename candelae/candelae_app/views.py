from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.


def check_json(request):
    return JsonResponse({"name": "Paul", "age": 22})


def home(request):
    return render(request, "home.html")
