from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("2023 InsyaAllah nikah. Aamiin!!!")

def index2(request):
    thisdict = {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': 1964
                }
    return JsonResponse(thisdict)