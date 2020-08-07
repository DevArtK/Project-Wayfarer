from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import UpdateView
from .models import UserProfile, City, Post
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth.models import User


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
    model = ProfileForm
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


# ----- User profile Page -----
# @login_required
def user_profile(request):
    return render(request, "user/detail.html")



# ------ User Signup Route ------
def signup(request):
    error = None
    form = RegistrationForm()
    context = {
        "form": form,
        "error": error,
    }
    if request.method == "POST":
        # Create an instance of Form
        profile_form = RegistrationForm(request.POST)  # !
        form = RegistrationForm(request.POST)
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


# User Profile Route
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': User,

    }
    return render(request, 'user/detail.html', context)
