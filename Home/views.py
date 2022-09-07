from Post.models import Post
from django.shortcuts import render
from User.models import UserProfile

# Create your views here.

def home(request):
    if request.method == "POST":
        text = request.POST.get('post')
        user = UserProfile.objects.get(user=request.user)
        if text is not None and text != '':
            newpost = Post(text=text, user=user)
            newpost.save()
            posts = Post.objects.all().order_by('-date')
            return render(request, 'home/index.html',{'posts':posts})

    else:
        posts = Post.objects.all().order_by('-date')
        return render(request, 'home/index.html',{'posts':posts})