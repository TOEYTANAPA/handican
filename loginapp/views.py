from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
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
def signup_success(request):
    return render(request, 'signup_success.html')


def job_signup(request):
    if request.method == 'POST':
        form = JobSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
           
            # form.save()
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user=User.objects.create_user(username=email, password=raw_password,email=email)
            user.save()
            user = authenticate(username=email,password=raw_password)
            login(request, user)
            my_group = Group.objects.get(name='disability') 
            my_group.user_set.add(user)
            # p = Profile(picture = request.FILES['image'],user=user,name=username,email=email)
            # p.save()
            # login(request, user)
            return redirect('job_signup2')
            # redirect process3
    else:
        form = JobSignUpForm()
    return render(request, 'job_signup.html', {'form': form})

def job_signup2(request):
    if request.method == 'POST':
        form = JobInformationForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
            print("request.user",request.user)
            profile = Profile.objects.create(user=request.user,profile_picture = request.FILES['profile_image'],)
            disability = DisabilityInfo.objects.create(
                profile = profile,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['first_name'],
                email = request.user.email,
                sex = form.cleaned_data['sex'],
                age = form.cleaned_data['age'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
                disability_cate = form.cleaned_data['disability_cate'],
                lastest_job = form.cleaned_data['lastest_job'],
                lastest_office = form.cleaned_data['lastest_office'],
                expected_salary = form.cleaned_data['expected_salary'],
                expected_welfare = form.cleaned_data['expected_welfare'],
                talent = form.cleaned_data['talent'],
                talent2 = form.cleaned_data['talent2'],
                talent3 = form.cleaned_data['talent3'],
                more_resume = request.FILES['more_resume'],
                get_more_info = form.cleaned_data['get_more_info'],
                )
            messages.success(request, "สมัครบัญชีผู้ใช้สำเร็จแล้ว")
            return redirect('signup_success')
            # redirect process3
    else:
        form = JobInformationForm()
    return render(request, 'job_signup2.html', {'form': form})

def company_signup(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
           
            # form.save()
            # username = form.cleaned_data.get('username')
            # username=
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user=User.objects.create_user(username=email, password=raw_password,email=email)
            user.save()
            user = authenticate(username=email,password=raw_password)
            login(request, user)
            my_group = Group.objects.get(name='company') 
            my_group.user_set.add(user)
            # p = Profile(picture = request.FILES['image'],user=user,name=username,email=email)
            # p.save()
            # login(request, user)
            return redirect('company_signup2')
            # redirect process3
    else:
        form = CompanySignUpForm()
    return render(request, 'company_signup.html', {'form': form})


def company_signup2(request):
    if request.method == 'POST':
        form = CompanyInformationForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
            profile = Profile.objects.create(user=request.user,profile_picture = request.FILES['company_image'],)
            comp = CompanyInfo.objects.create(
                profile =profile,
                th_name=form.cleaned_data['th_name'],
                en_name=form.cleaned_data['en_name'],
                info = form.cleaned_data['info'],
                website = form.cleaned_data['website'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
                fax = form.cleaned_data['fax'],
                company_type = form.cleaned_data['company_type'],
                get_more_info = form.cleaned_data['get_more_info'],
           
                )
        
            messages.success(request, "คุณได้สมัครบัญชีผู้ใช้สำเร็จแล้ว")

            return redirect('profile')
            # redirect process3
    else:
        form = CompanyInformationForm()
    return render(request, 'company_signup2.html', {'form': form})    

def profile(request):
    return render(request, 'profile.html')
