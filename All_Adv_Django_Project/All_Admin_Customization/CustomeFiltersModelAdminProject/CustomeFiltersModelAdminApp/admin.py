from django.contrib import admin
from .models import Blog
from django.contrib.admin import SimpleListFilter
# Register your models here.

class MySimpleFilter(SimpleListFilter):
    title="Pratik Filter"
    parameter_name="Title"
    def lookups(self,request,model_admin):
        return (
            ("has_roles","has_role"),
            ("no_roles","no_roles")
        )
    def queryset(self,request,queryset):
        if self.value()=="":
            return queryset
        if self.value()=="no_roles":
            return queryset.filter(roles="")
        if self.value()=="has_roles":
            return queryset.exclude(roles="")



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=["title","roles"]
    list_filter=["created_at","updated_at","roles",MySimpleFilter]
