from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

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
    # lazy 붙인이유: 바로나오는게 아니라 불러와줄때만 사용하기 위해
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
