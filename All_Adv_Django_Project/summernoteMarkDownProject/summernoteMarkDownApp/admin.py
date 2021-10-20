from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header="Blog Admin"
    site_title="Pratik Blog"
    index_title="Dashboard"


blog_site=BlogAdminArea(name="BlogAdmin")

class BlogSummerNoteAdmin(SummernoteModelAdmin):
    summernote_fields="description"


blog_site.register(Blog, BlogSummerNoteAdmin)

admin.site.register(Blog,BlogSummerNoteAdmin)
