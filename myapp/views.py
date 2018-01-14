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
from .forms import ContactForm
# Create your views here.
def home(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
	else :
		form = ContactForm()
	return render(request, 'home.html',{'username': request.user.username,'form':form})

def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

    return render(request, 'home.html',{'username': request.user.username})
def search(request):
    return render(request, 'search.html',{})

def employer_search(request):
    return render(request, 'employer_search.html',{})

def create_job(request):
    return render(request, 'create_job.html',{})

