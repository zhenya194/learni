from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Solution
from .forms import SolutionForm

def search(request):
    solutions = Solution.objects.filter(status='approved').order_by('-date_task')
    return render(request, "solutions/search.html", {"solutions": solutions})

def create(request):
    error = ""
    if request.method == "POST":
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save()
            solution.author = request.user
            solution.save()
            return redirect('solutions')
    else:
        form = SolutionForm()
        error = "Form is uncorrect."
    return render(request, "solutions/create.html", {
        "form": form,
        "error": error
    })

def requirements(request):
    return render(request, "solutions/requirements.html")

class SolutionDetail(DetailView):
    model = Solution
    template_name = 'solutions/solution.html'
    context_object_name = 'solution'

def send_to_review(request, solution_id):
    solution = get_object_or_404(Solution, id=solution_id)
    solution.save()
    return redirect('solutions')
