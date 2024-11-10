from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h1>home is a test <h1>')

def about_view(request):
    return HttpResponse('<h1>about is a test <h1>')

def contact_view(request):
    return HttpResponse('<h1>acontact is a test <h1>')
