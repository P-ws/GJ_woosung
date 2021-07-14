from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":   #POST으로 얻기

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()    #데이터가 실제로 DB에 저장 됨 (이 저장된 데이터를 반환해줌)

        return HttpResponseRedirect(reverse('accountapp:hello_world'))


    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html'
                      , context={'data_list': data_list})  # 중간부분만 쓸거니까 이부분만 불러와줌


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    templates_name = 'accountapp/create.html'