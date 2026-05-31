from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from .models import Lesson
from .forms import LessonForm

def search(request):
    prompt = request.GET.get("p")
    typ = request.GET.get("t")
    if prompt:
        if typ:
            lessons = Lesson.objects.filter(
                Q(title__icontains=prompt),
                Q(typ__icontains=typ),
                status="approved"
            ).order_by("-date")
        else:
            lessons = Lesson.objects.filter(
                Q(typ__icontains=typ),
                status="approved"
            ).order_by("-date")
    elif typ:
        prompt = ""
        lessons = Lesson.objects.filter(
            Q(typ__icontains=typ),
            status="approved"
        ).order_by("-date")
    else:
        lessons = Lesson.objects.filter(status='approved').order_by('-date')
        return render(request, "lessons/search.html", {
            "lessons": lessons
        })
    return render(request, "lessons/search.html", {
        "lessons": lessons,
        "prompt": prompt,
        "type": typ
    })

def create(request):
    error = ""
    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save()
            lesson.author = request.user
            lesson.save()
            return redirect('lessons')
        else:
            error = "Form is uncorrect."
    else:
        form = LessonForm()
    return render(request, "lessons/create.html", {
        "form": form,
        "error": error
    })

def requirements(request):
    return render(request, "lessons/requirements.html")

class LessonDetail(DetailView):
    model = Lesson
    template_name = 'lessons/lesson.html'
    context_object_name = 'lesson'

def send_to_review(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lesson.status = Lesson.Status.PENDING
    lesson.save()
    return redirect('lessons')
