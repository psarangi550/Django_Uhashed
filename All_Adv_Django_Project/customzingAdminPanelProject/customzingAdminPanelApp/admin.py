from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header="Blog Administration"

blog_site=BlogAdminArea(name="BlogAdmin")


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields="title"

blog_site.register(Blog,SummerAdmin)

# admin.site.register(Blog)
