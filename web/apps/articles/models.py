from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Article(models.Model):
    title = models.CharField("Title of lesson", max_length=150)
    description = models.CharField("Small text of article", max_length=200)
    text = models.TextField("Full text of article")
    image = models.FileField("Image for article", blank=True, validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])], upload_to="articles")
    date = models.DateTimeField("Date of publish", default=timezone.now)

    class Status(models.TextChoices):
        PENDING = 'pending'
        APPROVED = 'approved'
        REJECTED = 'rejected'

    reject_reason = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    