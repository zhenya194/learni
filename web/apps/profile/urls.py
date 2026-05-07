from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(
        template_name='profile/login.html', 
        redirect_authenticated_user=True,
        authentication_form=UserLoginForm
    ), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout')
]
