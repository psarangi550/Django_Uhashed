from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class BlogAdminAreaConfig(AdminConfig):
    default_site="summernoteMarkDownApp.admin.BlogAdminArea"



class SummernotemarkdownappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'summernoteMarkDownApp'
