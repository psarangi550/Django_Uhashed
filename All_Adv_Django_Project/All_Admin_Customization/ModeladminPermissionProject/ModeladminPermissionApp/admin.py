from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self,request,obj=None):
        print(obj)
        return obj
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

admin.site.register(Blog)
