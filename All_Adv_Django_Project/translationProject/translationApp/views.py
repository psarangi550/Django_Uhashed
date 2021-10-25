from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.
def index_view(request):
    lang=_("hello")
    return render(request, "translationApp/index.html", {"lang":lang})
