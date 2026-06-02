from django.shortcuts import render
from django.http import HttpResponse
from ..lessons.models import Lesson
from ..articles.models import Article

def index(request):
    lessons_count = Lesson.objects.filter(status="approved").count() - 11
    articles_count = Article.objects.filter(status="approved").count() - 11
    return render(
        request, "main/index.html",
        {
            "lessons_count": lessons_count,
            "articles_count": articles_count
        }
    )

def privacy(request):
    return render(request, "main/privacy.html")
