from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Subject(models.TextChoices):
    MATH = "math", "Math"
    PHYSICS = "physics", "Physics"

class Olympiad(models.Model):
    title = models.CharField("Time of year of olympiad", max_length=150)
    description = models.TextField("Description of olympiad")
    subject = models.CharField("Subject of olympiad", max_length=25, choices=Subject.choices)
    date = models.DateField("Date of publish", default=timezone.localdate)
    class Status(models.TextChoices):
        DRAFT = "draft",
        PUBLISHED = "published"
    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.DRAFT
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OlympiadTask(models.Model):
    olympiad = models.ForeignKey(Olympiad, on_delete=models.CASCADE, related_name="tasks")
    text = models.TextField("Text of olympiad's task")

class OlympiadTaskAnswer(models.Model):
    task = models.ForeignKey(OlympiadTask, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField("Text of olympiad's answer")
    is_true = models.BooleanField("Is answer true?", default=False)
