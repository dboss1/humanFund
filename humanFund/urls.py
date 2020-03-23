from django.urls import path

from . import views

urlpatterns = [
    path('', views.humanFund, name='humanFund'),
    path('humanFund/', views.humanFund, name='humanFund'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('portal/', views.portal, name='portal'),
]