from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    #로그인(html까지 설정) 로그아웃 경로 설정
    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # as.view 붙이면 class를 함수로봄?
    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]