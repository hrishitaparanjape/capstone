from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import User, Dream, Tag

def index(request):
    if request.user.is_authenticated:
        dreams = Dream.objects.filter(user=request.user).order_by('-date')
    else:
        dreams = Dream.objects.none()
    return render(request, "dream/index.html", {
        "dreams": dreams
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dream/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "dream/login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "dream/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "dream/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dream/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def new_dream(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        date = request.POST["date"]
        tags = request.POST.getlist("tags")
        emotional_state = request.POST["emotional_state"]
        dream = Dream(user=request.user, title=title, description=description, date=date, emotional_state=emotional_state)
        dream.save()
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            dream.tags.add(tag)
        dream.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        tags = Tag.objects.all()
        return render(request, "dream/new_dream.html", {
            "tags": tags
        })

@login_required
def dashboard(request):
    tags = request.GET.getlist("tags")
    emotional_state = request.GET.get("emotional_state")
    dreams = Dream.objects.filter(user=request.user)
    if tags:
        dreams = dreams.filter(tags__id__in=tags).distinct()
    if emotional_state:
        dreams = dreams.filter(emotional_state=emotional_state)
    return render(request, "dream/dashboard.html", {
        "dreams": dreams,
        "tags": Tag.objects.all()
    })