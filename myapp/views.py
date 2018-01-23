from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,Http404
from myapp.models import *
from django.views.generic.edit import UpdateView
# change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from datetime import date
from .forms import *
# Create your views here.
def home(request):

    if request.user.is_authenticated():

        if request.user.groups.filter(name='company').exists():
            return redirect('employer_search')
        else:
            return redirect('search')
    else :

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                email= form.cleaned_data.get('email')
                name = form.cleaned_data.get('name')
                phone= form.cleaned_data.get('phone')
                subject = form.cleaned_data.get('subject')
                message= form.cleaned_data.get('message')
                status = True

                Contact.objects.create(email=email,name=name,phone=phone,subject=subject,message=message)

            return render(request, 'home.html',{'username': request.user.username,'form':form,'status':status})


        else :
            form = ContactForm()    
    return render(request, 'home.html',{'username': request.user.username,'form':form})

    



def job_detail(request,job_name,job_id):
    # comp = CompanyInfo.objects.get(profile__user= request.user)
    job = Job.objects.get(title_th=job_name,id=job_id)
    


    return render(request, 'job_detail.html', {'job':job})

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

def notification_mobile(request):
    list_noti =[]
    try :
     
        noti = Notifications.objects.filter(user=request.user)
        for i in noti:
            
            temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False}
            
            try :
                dis = CompanyInfo.objects.get(profile=i.tarket)

                temp['name'] = dis.th_name
                temp['action'] = i.action
                temp['obj'] = i.obj
                temp['time'] = i.created_at
                temp['is_read'] = i.is_read
                temp['img'] = i.tarket.profile_picture.url
                if temp['is_read'] == False and read:
                    read = False

              
                list_noti.append(temp)
            except :
                comp = DisabilityInfo.objects.get(profile=i.tarket)
                temp['name'] = comp.first_name
                temp['action'] = i.action
                temp['obj'] = i.obj
                temp['time'] = i.created_at
                temp['is_read'] = i.is_read
                temp['img'] = i.tarket.profile_picture.url
                if temp['is_read'] == False and read:
                    read = False

              
                list_noti.append(temp)

            
    except :
        raise
    return render(request, 'notification_mobile.html',{'noti':list_noti})


def search(request):
    return render(request, 'search.html',{})

def employer_search(request):
    # dis_person = DisabilityInfo.objects.get(profile__user=request.user)

    if request.method == 'POST':
        form = CreateJobForm(request.POST, request.FILES)
        if form.is_valid():
            company = CompanyInfo.objects.get(profile__user=request.user)
            age1 = 0
            age2 = 0 
            salary1 = 0
            salary2 = 0
            if form.cleaned_data['age1'] >= form.cleaned_data['age2'] :
                age2 = form.cleaned_data['age1']
                age1 = form.cleaned_data['age2']
            if form.cleaned_data['salary1'] >= form.cleaned_data['salary2'] :
                salary2 = form.cleaned_data['salary1']
                salary1 = form.cleaned_data['salary2']
            cj = Job.objects.create(
                company =company,
                title_th=form.cleaned_data['title_th'],
                title_en=form.cleaned_data['title_en'],
                age1 = age1,
                age2 = age2,
                sex = form.cleaned_data['sex'],
                detail = form.cleaned_data['job_detail'],
                disability_cate = form.cleaned_data['disability_type'],
                traveling = form.cleaned_data['traveling'],
                welfare = form.cleaned_data['welfare'],
                salary1 = salary1,
                salary2 = salary2,
                company_image =request.FILES['company_image'],
           
                )
        
            messages.success(request, "คุณได้สร้างประกาศงานเรียบร้อยแล้ว")
            return HttpResponseRedirect('/employer-search/')


    else :
        form = CreateJobForm()

    return render(request, 'employer_search.html',{'form':form})

def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST, request.FILES)
        if form.is_valid():
            company = CompanyInfo.objects.get(profile__user=request.user)
            cj = Job.objects.create(
                company =company,
                title_th=form.cleaned_data['title_th'],
                title_en=form.cleaned_data['title_en'],
                age = form.cleaned_data['age'],
                sex = form.cleaned_data['sex'],
                detail = form.cleaned_data['job_detail'],
                disability_cate = form.cleaned_data['disability_type'],
                traveling = form.cleaned_data['traveling'],
                welfare = form.cleaned_data['welfare'],
                salary = form.cleaned_data['salary'],
                company_image =request.FILES['company_image'],
           
                )
        
            messages.success(request, "คุณได้สมัครบัญชีผู้ใช้สำเร็จแล้ว")
            redirect('employer_search')


    else :
        form = CreateJobForm()
    return render(request, 'create_job.html',{'form':form})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			email= form.cleaned_data.get('email')
			name = form.cleaned_data.get('name')
			phone= form.cleaned_data.get('phone')
			subject = form.cleaned_data.get('subject')
			message= form.cleaned_data.get('message')
			status = True

			Contact.objects.create(email=email,name=name,phone=phone,subject=subject,message=message)

		return render(request, 'contact.html',{'username': request.user.username,'form':form,'status':status})



	else :
		form = ContactForm()
	return render(request, 'contact.html',{'username': request.user.username,'form':form})
