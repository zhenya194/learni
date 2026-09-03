from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-of-use/', views.tou, name='tou'),
]
