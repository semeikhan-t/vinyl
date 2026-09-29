from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_user(request):
    return HttpResponse('hello world!')
