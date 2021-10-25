from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required,name=dispatch)
class MyProfileTemplate(TemplateView):
    template_name="registration/profile.html"

    # @method_decorator(login_required)
    # def dispath(self,*args,**kwargs):
    #     return super(dispatch, self).dispatch(*args,**kwargs)

decorators=[login_required,staff_member_required]
@method_decorator(decorators,name=dispatch)
class MyAboutTemplate(TemplateView):
    template_name="registration/about.html"
