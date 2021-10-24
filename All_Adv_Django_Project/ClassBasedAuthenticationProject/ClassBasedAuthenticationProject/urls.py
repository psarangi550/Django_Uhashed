"""ClassBasedAuthenticationProject URL Configuration

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
from ClassBasedAuthenticationApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.MyLoginView.as_view(),name="login"),
    path('dashboard/', views.MyDashboardView.as_view(),name="dashboard"),
    path('logout/', views.MyLogOutView.as_view(),name="logout"),
    path('changepass/', views.MyPasswordChangeView.as_view(),name="changepass"),
    path('changepassdone/', views.MyPasswordChangeDoneView.as_view(),name="changepassdone"),
    path('resetpass/', views.MyPasswordResetView.as_view(),name="resetpass"),
    path('resetpassdone/', views.MyPasswordResetDoneView.as_view(),name="resetpassdone"),
    path('resetpassconfirm/<uidb64>/<token>/',views.MyPasswordResetConfView.as_view(),name="password_reset_confirm"),
    path("resetpasscomplete/",views.MyPasswordResetComplete.as_view(),name="resetpasscomplete"),
]
