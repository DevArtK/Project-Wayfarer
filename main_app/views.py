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
    form = ProfileForm()
    context = {
        "form": form,
    }
    if request.method == "POST":
        # Create an instance of Form
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("/user/1")
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
    form = ProfileForm()
    context = {
        'form': form,
        'user': User,

    }
    return render(request, 'user/detail.html', context)

# CITIES = (

#     ('Austin, TX')
#     'Jacksonville, FL'
#     'Fort Worth, TX'
#     'San Francisco, CA'
#     'Columbus, OH'
#     'Charlotte, NC'
#     'Indianapolis, IN'
#     'Seattle, WA'
#     'Denver, CO'
#     'Washington, DC'
#     'El Paso, TX'
#     'Boston, MA '
#     'Nashville, TN '
#     'Portland, OR'
#     'Las Vegas, NV'
#     'Detroit, MI'
#     'Oklahoma City, TN'
#     'Memphis, TN'
#     'Louisville, KY'
#     'Baltimore, MD'
#     'Milwaukee, WI'
#     'Albuquerque, NM'
#     'Tucson, AZ'
#     'Fresno, CA'
#     'Sacramento, CA '
#     'Mesa, AZ'
#     'Atlanta, GA'
#    'Kansas City,'
#     'Colorado Springs,'
#     'Miami, FL'
#     'Raleigh, NC'
#     'Long Beach, CA'
#     'Virginia Beach, VA'
#     'Omaha, NE'
#     Oakland, CA
#     'Minneapolis, MN'
#     'Arlington, TX '
#     'Tampa, FL'
#     'Tulsa, OK'
#     'New Orleans,'

# )


def post_index(request):
    return render(request, 'post/index.html')
