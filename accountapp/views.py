from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    # return HttpResponse('Hell World')
    return render(request, 'accountapp/hell_world.html')
