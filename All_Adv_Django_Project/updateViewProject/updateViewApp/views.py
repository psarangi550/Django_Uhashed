from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Employee
from .forms import EmployeeForm
from django import forms
# from .forms import EmployeeForm
# Create your views here.
class EmpCreateView(CreateView):
    # model=Employee
    form_class=EmployeeForm
    # fields="__all__"
    # success_url="/thanks/"
    template_name="updateViewApp/employee_form.html"
    # def get_form(self):
    #     form=super().get_form()
    #     form.fields["ename"].widget=forms.TextInput(attrs={"placeholder":"Enter Your Name"})
    #     return form#return form object
class EmpUpdateView(UpdateView):
    # model=Employee
    queryset=Employee.objects.all()
    form_class=EmployeeForm
    # fields="__all__"
    template_name="updateViewApp/employee_form.html"
    # success_url="/thanks/"
    # def get_form(self):
    #     form=super().get_form()
    #     form.fields["ename"].widget=forms.TextInput(attrs={"placeholder":"Enter Your Name"})
    #     return form#return form object
