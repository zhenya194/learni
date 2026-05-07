from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='articles'),
    path('<int:pk>', views.ArticleDetail.as_view(), name='specArticle'),
    path('create/', views.create, name='createArticle'),
    path('create/requirements', views.requirements, name='reqArticles')
]
