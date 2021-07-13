from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":   #POST으로 얻기

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()    #데이터가 실제로 DB에 저장 됨 (이 저장된 데이터를 반환해줌)

        #데이터베이스 안의 모든 내용을 가져옴
        data_list = NewModel.objects.all()


        # 모델 데이터를 읽어옴
        return render(request, 'accountapp/hello_world.html'
                      , context={'data_list': data_list}) #중간부분만 쓸거니까 이부분만 불러와줌

    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/hello_world.html'
                      , context={'data_list': data_list})  # 중간부분만 쓸거니까 이부분만 불러와줌
