from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Employee
from django import forms
from .forms import EmployeeForm
from django.contrib import messages
from django.utils.text import slugify
from django.utils.translation import  gettext,gettext_lazy as _

# Create your views here.
class EmpCreateView(CreateView):
    # model=Employee
    form_class=EmployeeForm
    # fields="__all__"
    # success_url="/thanks/"
    template_name="CreateViewApp/employee_form.html"
    # def get_form(self):
    #     form=super().get_form()
    #     form.fields["ename"].widget=forms.TextInput(attrs={"placeholder":"Enter Your Name"})
    #     return form#return form object
    def post(self,request):
        messages.error(request, "object inserted successfully")
        return render(request, "CreateViewApp/thanks.html", )
