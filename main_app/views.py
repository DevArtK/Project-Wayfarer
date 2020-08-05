from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# from .models import
# from .forms import


# ----- HOME Route -----
def home(request):
    return render(request, "home.html")


# ----- ABOUT Route -----
def about(request):
    return render(request, "about.html")


# User Signup Route
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
      return redirect('index')
    else:
      return render(request, 'registration/signup.html', {'form': form, 'error': form.errors})
  else:
    return render(request, 'registration/signup.html', context)
