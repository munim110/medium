from Post.models import *
from django.shortcuts import render, redirect
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
            for post in posts:
                post.likes = post.likes.count()
            return render(request, 'home/index.html',{'posts':posts})

    else:
        posts = Post.objects.all().order_by('-date')
        return render(request, 'home/index.html',{'posts':posts, 'username':request.user.username})

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = UserProfile.objects.get(user=request.user)
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect(singlepost, post_id=post_id)


def singlepost(request, post_id):
    if request.method == "POST":
        text = request.POST.get('comment')
        user = UserProfile.objects.get(user=request.user)
        post = Post.objects.get(id=post_id)
        if text is not None and text != '':
            newcomment = Comment(text=text, user=user)
            newcomment.save()
            post.comments.add(newcomment)
            post.save()
            return redirect(singlepost, post_id=post_id)

    post = Post.objects.get(id=post_id)
    likes = post.likes.count()
    user = UserProfile.objects.get(user=request.user)
    all_likers = post.likes.all()
    print(all_likers)
    if user in post.likes.all():
        liked = True
    else:
        liked = False

    can_edit = request.user == post.user.user
    comments = post.comments.all().order_by('-date')
    return render(request, 'post/singlepost.html',{'post':post, 'liked':liked, 'likes':likes,
    'comments':comments, 'likers':all_likers, 'can_edit':can_edit, 'username':request.user.username})


def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    user = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        text = request.POST.get('post')
        if text is not None and text != '':
            post.text = text
            post.save()
            return redirect(singlepost, post_id=post_id)
    else:
        if post.user == user:
            return render(request, 'post/editpost.html',{'post':post})
        else:
            return redirect(singlepost, post_id=post_id)

def editComment(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    user = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        text = request.POST.get('comment')
        if text is not None and text != '':
            comment.text = text
            comment.save()
            return redirect(singlepost, post_id=post_id)
    else:
        if comment.user == user:
            return render(request, 'post/editcomment.html',{'comment':comment})
        else:
            return redirect(singlepost, post_id=post_id)

