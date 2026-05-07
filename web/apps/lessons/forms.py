from django.forms import ModelForm, TextInput, FileInput, Select, URLInput
from .models import Lesson

class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "video_url", "typ", "presentation", "document"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title of lesson"
            }),
            "video_url": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Youtube video"
            }),
            "typ": Select(attrs={
                "class": "form-control",
                "placeholder": "Type of lesson"
            }),
            "presentation": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Presentation file"
            }),
            "document": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Document file"
            })
        }
