from django.shortcuts import render,Http404
from .models import Blog
from django.views.generic import ListView
from django.http import Http404
# Create your views here.

class MyListView(ListView):
    template_name="paginationByClassBasedViewApp/index.html"
    ordering=["id"]
    model = Blog
    paginate_by=2
    paginate_orphans=1

    def get_context_data(self,*args, **kwargs):
        try:
            return super().get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs["page"]=1
            return super().get_context_data(*args, **kwargs)




