from django.contrib import admin
from .models import Blog
import django.apps
from django import forms
# Register your models here.


class BlogForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        ModelForm.__init__(self,*args,**kwargs)
        self.fields["author"].help_text="My Author"
    class Meta:
        model=Blog
        fields="__all__"





class BlogAdmin(admin.ModelAdmin):
    form_class=BlogForm
    fields=("author",)
    # fieldsets=(
    #         ("Section1",{"fields": ("title","author"),
    #         "classes":("collapse",),
    #         }),
    #         ("Section2",{"fields": ("description",),
    #         "classes":("collapse",),
    #         }),
    #     )
    # fields=[("title","author"),"description"]



admin.site.register(Blog,BlogAdmin)


print(django.apps.apps.get_models())

models=django.apps.apps.get_models()

for model in models:
    try:
        if admin.sites.AlreadyRegistered:
            pass
        else:
            admin.site.register(model)
    except:
        pass

