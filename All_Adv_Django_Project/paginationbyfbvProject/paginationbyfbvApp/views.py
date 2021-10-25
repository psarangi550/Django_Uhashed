from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.
def blog_view(request):
    blogs=Blog.objects.all()
    paginator=Paginator(blogs,2)
    page_number=request.GET.get("mypage")
    page_obj=paginator.get_page(page_number)
    return render(request,"paginationbyfbvApp/index.html",{"page_obj":page_obj})

def sing_blog_view(request,id):
    blog=Blog.objects.get(pk=id)
    return render(request, "paginationbyfbvApp/blog.html",{"page":blog})
