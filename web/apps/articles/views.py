from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm

def search(request):
    articles = Article.objects.filter(status='approved').order_by('-date')
    return render(request, "articles/search.html", {"articles": articles})

def create(request):
    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            article.author = request.user
            article.save()
            return redirect('articles')
        else:
            error = "Form is uncorrect."
    else:
        form = ArticleForm()
    return render(request, "articles/create.html", {
        "form": form,
        "error": error
    })

def requirements(request):
    return render(request, "articles/requirements.html")

class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'

def send_to_review(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.status = Article.Status.PENDING
    article.save()
    return redirect('articles')
