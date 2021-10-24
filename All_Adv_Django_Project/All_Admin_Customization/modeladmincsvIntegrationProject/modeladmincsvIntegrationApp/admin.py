from django.contrib import admin
from .models import Blog
from django import forms
from django.urls import path
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
# from django.template.response import TemplateResponse
# Register your models here.


class BlogCSVForm(forms.Form):
    csv_file_upload=forms.FileField()


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=["title","description"]
    base_template="admin/modeladmincsvIntegrationApp/blog/base.html"
    # base="modeladmincsvIntegrationApp/admin/base.html"

    def csv_file(self,request):
        return render(request,"admin/modeladmincsvIntegrationApp/blog/upload_csv.html")
        # return ("hello")

    def get_urls(self):
        old_urls=super().get_urls()
        my_url=[path("csv_file/", self.csv_file),]
        return my_url+old_urls

    def csv_file(self,request):
        form=BlogCSVForm()
        if request.method == "POST":
            my_csv_data=request.FILES["csv_file_upload"]
            # print(my_csv_data)
            data=my_csv_data.read().decode("utf-8")
            ext=data.split(",")
            for d in data:
                Blog.objects.update_or_create(title=ext[0],description=ext[1])
        return render(request,"admin/modeladmincsvIntegrationApp/blog/upload_csv.html",{"form":form})
        # return HttpResponse("hello")




