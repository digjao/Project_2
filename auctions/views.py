import re
from auctions.forms import Newlist
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

from .models import Category, Listing, User





def index(request):
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all()
    })

def item(request, item_id):
    item = Listing.objects.get(pk=item_id)
    return render(request, "auctions/item.html", {
        "item": item
    })     

# def newlist(request):
#      if request.method == "POST"
#         f = (title=reques.POST["title"]
#               category = request.POST["category"]
#               description = request.POST["description"] )   
#         }
#         return render(request, "auctions/newlist.html",)

@login_required
def newlist(request):
        return render(request, "auctions/newlist.html", {
            "form": Newlist(),})

@login_required
def savelist(request):
    print("entrei aqui antes")
    if request.method == "POST":
        form = Newlist(request.POST)
        print("entrei aqui")
        if form.is_valid():
            listing = form.save()
            listing.creator = request.user
            listing.save()
            return HttpResponseRedirect(reverse("item", kwargs={'item_id': listing.id}))
            

        



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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
