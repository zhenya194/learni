from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import LetsDoItAnyway
from .forms import LetsDoItAnywayForm

def search(request):
    solutions = LetsDoItAnyway.objects.filter(status='approved').order_by('-date_task')
    return render(request, "letsdoitanyway/search.html", {"solutions": solutions})

def create(request):
    error = ""
    if request.method == "POST":
        form = LetsDoItAnywayForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save()
            solution.author = request.user
            solution.save()
            return redirect('solutions')
    else:
        form = LetsDoItAnywayForm()
        error = "Form is uncorrect."
    return render(request, "letsdoitanyway/create.html", {
        "form": form,
        "error": error
    })

def requirements(request):
    return render(request, "letsdoitanyway/requirements.html")

class SolutionDetail(DetailView):
    model = LetsDoItAnyway
    template_name = 'letsdoitanyway/solution.html'
    context_object_name = 'solution'

def send_to_review(request, solution_id):
    solution = get_object_or_404(LetsDoItAnyway, id=solution_id)
    solution.save()
    return redirect('solutions')
