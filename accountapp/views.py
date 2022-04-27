from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

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

        #4. 새로고침 시 반복적으로 POST 기능이 수행되지 않도록, accountapp:hell_world 로의 라우팅에 'redirect' 기능을 사용
        return HttpResponseRedirect(reverse('accountapp:hell_world'))
    else:
        # 3. 데이터베이스의 HellWorld 객체의 모든 리스트를 추출
        hell_world_list = HellWorld.objects.all()
        return render(request, 'accountapp/hell_world.html', context={'showAll': hell_world_list})

class AccountCreateView(CreateView):
    # Django에서 기본 제공하는 모델인 User
    model = User
    # Django에서 기본 제공하는 User 생성 폼
    form_class = UserCreationForm
    # reverse()는 함수형 베이스 뷰에서, reverse_lazy는 클래스형 베이스 뷰에서 사용
    success_url = reverse_lazy('accountapp:hell_world')
    template_name = 'accountapp/create.html'