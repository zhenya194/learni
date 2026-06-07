from django.db import models
from django.utils import timezone
from ..articles.models import Article

class News(models.Model):
    title = models.CharField("Title of news", max_length=150)
    text = models.TextField("Text of news")
    date = models.DateField("Date of publish", default=timezone.now)
    icon = models.CharField("FA icon", default="fa-solid fa-cubes", max_length=120)
