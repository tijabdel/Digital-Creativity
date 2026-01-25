from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignupForm
from housing.models import BookingRequest

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url or "dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")



def logout_view(request):
    logout(request)
    return redirect("city_list")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def dashboard(request):
    requests = (
        BookingRequest.objects
        .filter(student=request.user)
        .select_related("room", "room__house", "room__house__city")
        .order_by("-created_at")
    )
    return render(request, "accounts/dashboard.html", {"requests": requests})
