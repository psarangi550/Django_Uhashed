from django import forms #importing the forms from the django module
from .models import Employee #importing the Employee Model
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
