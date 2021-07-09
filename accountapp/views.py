from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    if request.method == "POST":   #POST으로 얻기
        return render(request, 'accountapp/hello_world.html'
                      , context={'text': 'POST METHOD!'}) #중간부분만 쓸거니까 이부분만 불러와줌

    else:
        return render(request, 'accountapp/hello_world.html'
                      , context={'text': 'GET METHOD!'}) #이건 get으로 얻기
