from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
# Create your views here.
@login_required(redirect_field_name="user")
def user_profile(request):
    return render (request,"registration/profile.html")

@staff_member_required()
def user_about(request):
    return render(request,"registration/about.html")

@permission_required("decoratorsApp.change_user",raise_exception=False)
def user_perms(request):
    return render(request,"registration/service.html")


