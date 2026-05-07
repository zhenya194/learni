from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from .models import Profile
from .forms import UserRegisterForm
from django.urls import reverse_lazy

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile/profile.html"
    login_url = reverse_lazy("login")

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "profile/register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.save()
        Profile.objects.get_or_create(user=user)
        login(self.request, user)
        return redirect(self.success_url)
    

def logout_view(request):
    logout(request)
    return redirect('login')
