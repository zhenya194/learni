from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='lessons'),
    path('<int:pk>', views.LessonDetail.as_view(), name='specLesson'),
    path('create/', views.create, name='createLesson'),
    path('create/requirements', views.requirements, name='reqLesson')
]
