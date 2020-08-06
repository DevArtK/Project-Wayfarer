from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import ProfileForm, AuthenticationForm
from django.views.generic import UpdateView
from .models import UserProfile, City, Post
from .forms import RegistrationForm, ProfileForm


class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location


City = [
    City("Atlanta", "GA"),
    City("Norwalk", "CT"),
    City("Brooklyn", "NY"),
]

# ----- User Reg + User Profile


class ProfilView(UpdateView):
    model = UserProfile
    fields = ["first_name", "last_name", "picture", "location"]
    template_name = 'registration/signup'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user

# ----- HOME Route -----


def home(request):
    return render(request, "home.html")


# ----- ABOUT Route -----
def about(request):
    return render(request, "about.html")


# ------ User Signup Route ------
def signup(request):
    error = None
    form = ProfileForm()
    context = {
        "form": form,
        "error": error,
    }
    if request.method == "POST":
        # Create an instance of Form
        profile_form = ProfileForm(request.POST)  # !
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                "registration/signup.html",
                {"form": form, "error": form.errors},
            )
    else:
        return render(request, "registration/signup.html", context)
