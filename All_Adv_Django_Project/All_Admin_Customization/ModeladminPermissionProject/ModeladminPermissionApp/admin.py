from django.contrib import admin
from .models import Blog,Book
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# Register your models here.

class BlogModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self,request,obj=None):
        if request.user.groups.filter(name="Editor").exists():
            return True
        return True
    def has_add_permission(self,request,obj=None):
        return True
    def has_view_permission(self,request,obj=None):
        return True
    def has_change_permission(self,request,obj=None):
        return True


class BlogAdminArea(admin.AdminSite):
    site_header="Blog Admin Area Login"
    index_title="Pratik's Blog Application"

blog_site=BlogAdminArea(name="BlogAdmin")

blog_site.register(Blog,BlogModelAdmin)
# blog_site.register(User)
# blog_site.register(Group)
blog_site.register(Book,BlogModelAdmin)

admin.site.register(Blog)
