from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Olympiad

def search(request):
    olympiads = Olympiad.objects.all().order_by("-date")
    return render(request, "olympiads/search.html",
                  {"olympiads": olympiads})

class OlympiadDetail(DetailView):
    model = Olympiad
    template_name = "olympiads/olympiad.html"
    context_object_name = "olympiad"
