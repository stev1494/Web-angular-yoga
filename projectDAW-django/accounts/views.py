from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request,'userprofile.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def userprofile(request):
	return render(request,'userprofile.html')
