from django.forms import ModelForm, TextInput, FileInput
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "text", "image"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title of article"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Small text of article"
            }),
            "text": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Full text of article"
            }),
            "image": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Image for article"
            }),
        }
