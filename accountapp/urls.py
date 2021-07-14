from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    # as.view 붙이면 class를 함수로봄?
    path('create/', AccountCreateView.as_view(), name='create')
]