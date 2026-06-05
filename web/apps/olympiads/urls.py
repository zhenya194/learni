from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='olympiads'),
    path('<int:pk>', views.olympiad_detail, name='olympiad'),
]
