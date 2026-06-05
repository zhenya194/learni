from django.shortcuts import render, get_object_or_404
from .models import Olympiad

def search(request):
    olympiads = Olympiad.objects.all().order_by("-date")
    return render(request, "olympiads/search.html",
                  {"olympiads": olympiads})

def olympiad_detail(request, pk):
    olympiad = get_object_or_404(Olympiad, pk=pk)
    error: str = ""
    true_answers_count: int = 0
    true_answers_hundred: int = 0
    if request.method == "POST":
        try:
            for task in olympiad.tasks.all():
                answer_id = request.POST.get(f"task{task.id}")[0]
                if task.answers.get(pk=int(answer_id)).is_true:
                    true_answers_count += 1
            point_per_question = 100 / olympiad.tasks.all().count()
            true_answers_hundred = true_answers_count * point_per_question
        except KeyError:
            error = "Please, answer on all tasks."
        except:
            error = "An error occured."
    return render(request, "olympiads/olympiad.html", {
        "olympiad": olympiad,
        "true_answers_count": true_answers_count,
        "true_answers_hundred": true_answers_hundred,
        "error": error,
    })
