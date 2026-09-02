from django.db import models
from django.contrib.auth.models import User
from ..olympiads.models import Olympiad


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    completed_olympiads = models.ManyToManyField(Olympiad, related_name="completed_olympiads", blank=True)
