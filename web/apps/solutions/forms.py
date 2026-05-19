from django.forms import ModelForm, TextInput, FileInput, URLInput, DateInput
from .models import Solution

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = ["title", "task_url", "url_github", "url_gitlab", "url_dropbox", "url_googledrive", "url_mega", "torrent", "date_task"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title of solution"
            }),
            "task_url": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to task"
            }),
            "url_github": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Github repo or tag(release)"
            }),
            "url_gitlab": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Gitlab repo or tag(release)"
            }),
            "url_dropbox": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Dropbox files"
            }), 
            "url_googledrive": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Google Drive files"
            }),
            "url_mega": URLInput(attrs={
                "class": "form-control",
                "placeholder": "URL to Mega Drive files"
            }),
            "torrent": FileInput(attrs={
                "class": "form-control",
                "placeholder": ".torrent file"
            }),
            "date_task": DateInput(attrs={
                "class": "form-control",
                "placeholder": "Date when task published"
            }),
        }
