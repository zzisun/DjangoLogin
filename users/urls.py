from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('signup/', views.registerPage, name='registerPage'),
    path('verify/',views.verifyAccount, name='verify')
]