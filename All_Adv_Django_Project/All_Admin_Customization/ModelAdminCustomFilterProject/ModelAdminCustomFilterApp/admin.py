from django.contrib import admin
from.models import Profile
from django.contrib.admin import SimpleListFilter
# Register your models here.

class CustFilter(SimpleListFilter):
    title="Model Filter"
    parameter_name="user_full"
    def lookups(self,request,model_admin):
        return  [
           ("has_email","has_email"),
            ("no_email", "no_email"),
        ]
    def queryset(self,request,queryset):
        if self.value()=='':
            return queryset
        if self.value()=="has_email":
            return queryset.exclude(user__email="")
        if self.value()=="no_email":
            return queryset.filter(user__email="")

class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","email","full_name","roles","is_active","created_at","updated_at"]
    list_filter=["is_active","created_at","roles",CustFilter]





admin.site.register(Profile,ProfileAdmin)
