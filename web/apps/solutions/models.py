from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Solution(models.Model):
    title = models.CharField("Title of solution", max_length=150)
    task_url = models.URLField("URL to task", blank=True, null=True)
    url_github = models.URLField("URL to Github repo or tag(release)")
    url_gitlab = models.URLField("URL to Gitlab repo or tag(release)", blank=True, null=True)
    url_dropbox = models.URLField("URL to Dropbox files", blank=True, null=True)
    url_googledrive = models.URLField("URL to Google Drive files", blank=True, null=True)
    url_mega = models.URLField("URL to Mega Drive files", blank=True, null=True)
    torrent = models.FileField(".torrent file",
                                upload_to="solutions/torrent",
                                validators=[FileExtensionValidator(allowed_extensions=["torrent"])],
                                blank=True,
                                null=True)
    date_task = models.DateField("Date when task was published")
    date_published = models.DateField("Date of publish", default=timezone.now)

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
