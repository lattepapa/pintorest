from django.http import HttpResponse
from django.shortcuts import render

def hell_world(request):
    # return HttpResponse('Hell World')
    if request.method == "POST":
        return render(request, 'accountapp/hell_world.html', context={'isAllowed': 'POST METHOD!!!'})
    else :
        return render(request, 'accountapp/hell_world.html')
