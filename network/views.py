from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import User, Post, Like, Follow
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt   
import json

def index(request):
    if request.method == "POST":
        user = request.user
        text = request.POST.get("text")
        timestamp = datetime.now()

        post = Post()
        post.user = user
        post.text = text
        post.timestamp = timestamp
        post.likes = 0
        post.save()

    posts = Post.objects.all().order_by('-timestamp')

    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.save()
        print(post.getLikes())

    pages = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    return render(request, "network/index.html", {
        "page_obj": page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, id):
    user = User.objects.get(id=id)
    diff_person = True

    if user == request.user:
        diff_person = False

    if request.method == "POST":
        if Follow.objects.filter(follower=request.user, followee=user).count() == 0:
            follow = Follow()
            follow.follower = request.user
            follow.followee = user
            follow.save()
            following = True
        else:
            follow = Follow.objects.filter(follower=request.user, followee=user)
            follow.delete()
            following = False
    else:
        if Follow.objects.filter(follower=request.user, followee=user).count() == 0:
            following = False
        else:
            following = True

    followers = Follow.objects.filter(followee=user).count()
    followees = Follow.objects.filter(follower=user).count()
    posts = Post.objects.filter(user=user).order_by('-timestamp')

    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.save()

    pages = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    return render(request, "network/profile.html", {
        "owner": user,
        "lurker": request.user,
        "following": following,
        "diff_person": diff_person,
        "followers": followers,
        "followees": followees,
        "page_obj": page_obj
    })
    
def following(request):
    following = Follow.objects.filter(follower=request.user)

    posts = []

    for follow in following:
        posts += Post.objects.filter(user=follow.followee)


    print(posts)

    for post in posts:
        post.likes = Like.objects.filter(post=post.id).count()
        post.save()

    pages = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    return render(request, "network/following.html", {
        "page_obj": page_obj
    })

@csrf_exempt
def edit(request, id):
    if request.method == "PUT":
        post = Post.objects.get(id=id)
        post.text = json.loads(request.body).get("text")
        post.save()
        return HttpResponse(status=200)

@csrf_exempt
def like(request, id):
    if request.method == "PUT":
        liked = json.loads(request.body).get("liked")
        post = Post.objects.get(id=id)
        if liked:
            like = Like()
            like.user = request.user
            like.post = post
            like.save()
            return HttpResponse(status=200)
        else:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return HttpResponse(status=200)