from django.shortcuts import render
from .models import Images

# Create your views here.
def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images

        
    return render(request, 'index.html',context)