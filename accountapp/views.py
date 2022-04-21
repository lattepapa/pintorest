from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HellWorld


def hell_world(request):
    # return HttpResponse('Hell World')
    if request.method == "POST":
        # 1. 텍스트 input 창에 입력된 값을 temp 변수에 저장
        temp = request.POST.get('hell_world_input')

        # 2. 데이터베이스에 temp 변수 값 저장
        new_hell_world = HellWorld()
        new_hell_world.testText = temp
        new_hell_world.save()

        return render(request, 'accountapp/hell_world.html', context={'isClicked': new_hell_world})
    else:
        return render(request, 'accountapp/hell_world.html')
