from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import UpdateView
from .models import UserProfile, City, Post
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
@login_required
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    form = ProfileForm()
    context = {
        'form': form,
        'user': User,

    }
    return render(request, 'user/detail.html', context)

# User Profile edit
@login_required
def  user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user - form.save()
            return redirect('user', user.id)
    else:
        form = UserForm(request.POST, instance=user)
        return render(request, 'user/edit.html', {'form': form})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'post/detail.html', context)




# Post Index Route
def post_index(request):
    return render(request, 'post/index.html')