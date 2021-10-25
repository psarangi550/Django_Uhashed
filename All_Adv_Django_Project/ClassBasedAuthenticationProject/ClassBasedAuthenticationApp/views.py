from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordChangeView,PasswordResetDoneView,PasswordChangeDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.views.generic.base import TemplateView
from .forms import MyAuthForm
from django.urls import  reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

class MyLoginView(LoginView):
    template_name="ClassBasedAuthenticationApp/login.html"
    form_class=MyAuthForm

class MyDashboardView(TemplateView):
    template_name="ClassBasedAuthenticationApp/dashboard.html"

class MyLogOutView(LogoutView):
    template_name="ClassBasedAuthenticationApp/logout.html"

class MyPasswordChangeView(PasswordChangeView):
    template_name="ClassBasedAuthenticationApp/changepass.html"
    success_url="/changepassdone/"

class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name="ClassBasedAuthenticationApp/changepassdone.html"

class MyPasswordResetView(PasswordResetView):
    template_name="ClassBasedAuthenticationApp/resetpass.html"
    success_url=reverse_lazy("resetpassdone")
    # subject_template_name="password forgot again"

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name="ClassBasedAuthenticationApp/resetpassdone.html"

class MyPasswordResetConfView(PasswordResetConfirmView):
    success_url=reverse_lazy("resetpasscomplete")
    template_name="ClassBasedAuthenticationApp/resetpassconf.html"

class MyPasswordResetComplete(PasswordResetCompleteView):
    template_name="ClassBasedAuthenticationApp/resetpasscomplete.html"
