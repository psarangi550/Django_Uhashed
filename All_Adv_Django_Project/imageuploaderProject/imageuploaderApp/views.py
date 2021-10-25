from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def image_view(request):
    img=Image.objects.all().order_by("-id")
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=ImageForm()
    else:
        form=ImageForm()
    return render(request,"imageuploaderApp/image.html",{"form":form,"img":img})
