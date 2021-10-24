from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header="Blog Admin Area"
    login_template="CustomizeAdminLoginPageApp/admin/login.html"

blog_site=BlogAdminArea(name="BlogAdmin")

blog_site.register(User)
