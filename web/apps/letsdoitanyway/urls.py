from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='solutions'),
    path('<int:pk>', views.SolutionDetail.as_view(), name='specSolution'),
    path('create/', views.create, name='createSolution'),
    path('create/requirements', views.requirements, name='reqSolution')
]
