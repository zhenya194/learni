from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..lessons.models import Lesson
from ..articles.models import Article
import datetime
import random

def index(request: HttpRequest) -> HttpResponse:
    lessons_count = Lesson.objects.filter(status="approved").all().count()
    articles_count = Article.objects.filter(status="approved").all().count()

    articles = list(Article.objects.filter(status="approved").all())
    random.shuffle(articles)
    random_articles = articles[:3]

    lessons = list(Lesson.objects.filter(status="approved").all())
    random.shuffle(lessons)
    random_lessons = lessons[:2]

    return render(
        request, "main/index.html",
        {
            "lessons_count": lessons_count,
            "articles_count": articles_count,
            "random_articles": random_articles,
            "random_lessons": random_lessons,
            "timezone": "UTC",
            "time": f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}",
        }
    )


def privacy(request: HttpRequest) -> HttpResponse:
    return render(request, "main/privacy.html")

def tou(request: HttpRequest) -> HttpResponse:
    return render(request, "main/tou.html")
