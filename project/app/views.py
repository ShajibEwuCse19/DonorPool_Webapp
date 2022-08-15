from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from .models import User


# Home Page
def home(request):
    diction = {}
    return render(request, "app/home.html", context=diction)


# signup
def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "app/signup.html", context)


def profile_view(request):
    user = User.objects.get(id=request.user.id)
    form = UserProfileForm(request.POST or None, instance=user)

    context = {"user": user, "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, "app/profile.html", context)


def delete_profile(request, id):

    if request.method == "POST" and request.user.id == id:
        user = User.objects.get(id=id)
        user.delete()
        return redirect(reverse("home"))
