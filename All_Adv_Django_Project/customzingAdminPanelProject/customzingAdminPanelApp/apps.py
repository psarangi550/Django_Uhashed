from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

# class MyConfig(AdminConfig):
#     default_site="customzingAdminPanelApp.admin.BlogAdminArea"

class CustomzingadminpanelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customzingAdminPanelApp'
