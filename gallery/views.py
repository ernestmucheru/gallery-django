from django.shortcuts import render
from .models import Images,Category, Location
from django.core.mail import EmailMessage
from django.http import Http404
# from django.core.exceptions import DoesNotExist

# Create your views here.
def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images
    # categories = Category.objects.all()
    # context = {'categories': categories}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject =request.POST.get("subject")
        message = request.POST.get("message")
        category = request.GET.get("category")
        location = request.POST.get("location")

        if category == None:
            images = Images.objects.all()
        else:
            images = Images.objects.filter(category__name=category)

            categories = Category.objects.all()
            images = Images.objects.all()
            
        email_message = EmailMessage(
            subject = name + " : " +subject,
            body = message,
            to = ['your gmail'],
            headers = {"Reply-To": email}
        )
        email_message.send()

        
    return render(request, 'index.html',context)

def viewPhoto(request, id):
    try:
        images = Images.objects.get(id=id)
    except Images.DoesNotExist:
        raise Http404()
    return render(request, 'gallery/photo.html',{'image':images})
def addPhoto(request):
    return render(request, 'gallery/add.html')