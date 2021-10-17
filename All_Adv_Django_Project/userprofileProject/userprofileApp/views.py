from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import Register,ProfileUserChange
from django.contrib.auth.models import User,Group
# Create your views here.

#user register
####################
def user_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=Register(request.POST)
            if form.is_valid():
                Author=Group.objects.get(name="Author")
                user=form.save()
                user.groups.add(Author)
                # user.save()
            return HttpResponseRedirect("/login/")
        form=Register()
        return render(request,"userprofileApp/register.html",{"form":form})
    else:
         return HttpResponseRedirect('/profile/')
#user login
####################
def user_login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(request,username=uname,password=password)
                if user is not None:
                    login(request,user)
                return HttpResponseRedirect("/profile/")
        else:
            form=AuthenticationForm()
        return render(request, "userprofileApp/login.html" , {"form":form})
    else:
        return HttpResponseRedirect("/profile/")
#user logout
####################
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/register/")
    else:
        return HttpResponseRedirect("/login/")
#profile_page
###########################
def profile(request):
    if request.user.is_authenticated:
        return render(request, "userprofileApp/profile.html")
    else:
        return HttpResponseRedirect("/login/")

#passwordchange
#---------------------

def user_pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request, "userprofileApp/passchange.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")


#user_profile_change
#---------------------------
def user_profile_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=ProfileUserChange(instance=request.user,data=request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/profile/")
        else:
            form=ProfileUserChange(instance=request.user)
        return render(request, "userprofileApp/profilechange.html", {"form":form})
    else:
        return HttpResponseRedirect("/login/")



