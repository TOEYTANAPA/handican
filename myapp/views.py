from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from myapp.models import *
from django.views.generic.edit import UpdateView
# change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from datetime import date
# Create your views here.
def home(request):
    return render(request, 'home.html',{'username': request.user.username})
def search(request):
    return render(request, 'search.html',{})

def employer_search(request):
    return render(request, 'employer_search.html',{})

def create_job(request):
    return render(request, 'create_job.html',{})
