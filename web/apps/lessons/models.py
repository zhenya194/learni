from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

LESSON_TYPES = [
    ('video', 'Video lesson'),
    ('presentation', 'Presentation'),
    ('document', 'Document'),
]

class Lesson(models.Model):
    title = models.CharField("Title of lesson", max_length=150)
    typ = models.CharField("Type of lesson", max_length=50, choices=LESSON_TYPES)
    video_url = models.URLField("URL to Youtube video", blank=True)
    presentation = models.FileField(
        "Presentation file",
        upload_to="lessons/presentations",
        validators=[FileExtensionValidator(allowed_extensions=["pptm", "pptx", "odp", "key", "pdf"])],
        blank=True
    )
    document = models.FileField(
        "Document file",
        upload_to="lessons/docs",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "docm", "odt", "pdf"])],
        blank=True
    )
    date = models.DateTimeField("Date of publish", default=timezone.now)

    class Status(models.TextChoices):
        DRAFT = 'draft'
        PENDING = 'pending'
        APPROVED = 'approved'
        REJECTED = 'rejected'

    reject_reason = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )

    def clean(self):
        super().clean()

        has_video = bool(self.video_url)
        has_pres = bool(self.presentation)
        has_doc = bool(self.document)
        if not (has_video or has_pres or has_doc):
            raise ValidationError("At least one field must be filled in.")

        if self.typ == 'video':
            if not has_video:
                raise ValidationError("For video lesson you need to provide a link.")
            if has_pres or has_doc:
                raise ValidationError("For video lesson you need to provide a link.")

        elif self.typ == 'presentation':
            if not has_pres:
                raise ValidationError("You need to upload a presentation.")
            if has_video or has_doc:
                raise ValidationError("You need to upload a presentation.")

        elif self.typ == 'document':
            if not has_doc:
                raise ValidationError("You need to upload a document.")
            if has_video or has_pres:
                raise ValidationError("You need to upload a document.")
