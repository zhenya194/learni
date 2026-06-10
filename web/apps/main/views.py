from django.shortcuts import render
from ..lessons.models import Lesson
from ..articles.models import Article
import random

def index(request):
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
        }
    )

def privacy(request):
    return render(request, "main/privacy.html")
