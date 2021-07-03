from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return render(request, 'accountapp/hello_world.html') #중간부분만 쓸거니까 이부분만 불러와줌
