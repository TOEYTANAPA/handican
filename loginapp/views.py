from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from myapp.models import *
from loginapp.forms import *
# change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import Http404

# Create your views here.
def signup(request):
    return render(request, 'signup.html', {'form': form})

def choose_signup(request):
    return render(request, 'choose_signup.html')


def job_signup(request):
    if request.method == 'POST':
        form = JobSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
           
            form.save()
            username = form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # p = Profile(picture = request.FILES['image'],user=user,name=username,email=email)
            # p.save()
            # login(request, user)
            # return redirect('login')
            # redirect process3
    else:
        form = JobSignUpForm()
    return render(request, 'job_signup.html', {'form': form})

def company_signup(request):
    return render(request, 'choose_signup.html')