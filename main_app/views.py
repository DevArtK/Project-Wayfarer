from django.shortcuts import render, HttpResponse, redirect
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User, Post, City
=======
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
>>>>>>> 5e8122f636fdee829a30fc4eb2b07e3957d39ed4

# from .forms import

# TEMP CAT DATA
class City: 
     def __init__(self, name, location):
       self.name = name
       self.location = location

City = [
     City('Atlanta', 'GA'),
     City('Norwalk', 'CT'),
     City('Brooklyn', 'NY'),
]

# ----- HOME Route -----
def home(request):
    return render(request, "home.html")


# ----- ABOUT Route -----
def about(request):
    return render(request, "about.html")


# ------ User Signup Route ------
def signup(request):
  error = None
  form = UserCreationForm()
  context = {
    'form': form,
    'error': error,
  }
  if request.method == 'POST':
    # Create an instance of Form
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
  else:
    return render(request, 'registration/signup.html', context)
