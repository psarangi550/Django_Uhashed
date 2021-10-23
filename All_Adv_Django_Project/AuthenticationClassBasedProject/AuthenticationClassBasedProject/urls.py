"""AuthenticationClassBasedProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
urlpatterns = [
    path('admin/', admin.site.urls),

    path("login/",auth_views.LoginView.as_view(template_name="AuthenticationClassBasedApp/login.html"),
        name="login"),

    path("dashboard/", TemplateView.as_view(template_name="AuthenticationClassBasedApp/dashboard.html"),name="dashboard"),

    path("logout/",auth_views.LogoutView.as_view(template_name="AuthenticationClassBasedApp/logout.html"),
        name="logout"),

    path("changepass/",auth_views.PasswordChangeView.as_view(template_name="AuthenticationClassBasedApp/changepass.html",success_url="/changepassdone/"),name="rchangepass"),

     path("changepassdone/",auth_views.PasswordChangeDoneView.as_view(template_name="AuthenticationClassBasedApp/changepassdone.html"),name="rchangepassdone"),

    path("resetpass/",auth_views.PasswordResetView.as_view(template_name="AuthenticationClassBasedApp/resetpass.html",success_url=reverse_lazy("resetpassdone")),name="resetpass"),

    path("resetpassdone/",auth_views.PasswordResetDoneView.as_view(template_name="AuthenticationClassBasedApp/resetpassdone.html"),name="resetpassdone"),

    path("resetpassconfirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="AuthenticationClassBasedApp/resetpassconf.html",success_url=reverse_lazy("resetpasscomplete")),name="password_reset_confirm"),

    path("resetpasscomplete/",auth_views.PasswordResetCompleteView.as_view(template_name="AuthenticationClassBasedApp/resetpasscomplete.html"),name="resetpasscomplete"),

]
