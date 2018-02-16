from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.contrib.auth.models import Group
from myapp.models import *
from loginapp.forms import *
# change password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def signup(request):
    return render(request, 'signup.html', {'form': form})

def choose_signup(request):
    return render(request, 'choose_signup.html')
def signup_success(request):
    return render(request, 'signup_success.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        # else:
        #     messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


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
            # login(request, user)
            
            my_group = Group.objects.get(name='disability') 
            my_group.user_set.add(user)
            # p = Profile(picture = request.FILES['image'],user=user,name=username,email=email)
            # p.save()
            # login(request, user)

            # return redirect('job_signup2')
            return redirect('job_signup2', uid=user.id)
     
    else:
        form = JobSignUpForm()
    return render(request, 'job_signup.html', {'form': form})

def job_signup2(request,uid):
    if request.method == 'POST':
        form = JobInformationForm(request.POST,request.FILES or None)
        if form.is_valid():
            print("Earn")
            user = User.objects.get(id=uid)
            print(user)
            try:
                more_resume = request.FILES['more_resume']
            except Exception as e:
                more_resume = None
            expected_salary1 = 0 
            expected_salary2 = 0   
            if form.cleaned_data['expected_salary1'] >= form.cleaned_data['expected_salary2']:
                expected_salary1 = form.cleaned_data['expected_salary2']
                expected_salary2 = form.cleaned_data['expected_salary1']
            else:
                expected_salary1 = form.cleaned_data['expected_salary1']
                expected_salary2 = form.cleaned_data['expected_salary2']

            profile = Profile.objects.create(user=user,profile_picture = request.FILES['profile_image'],)
            disability = DisabilityInfo.objects.create(
                profile = profile,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email = user.email,
                sex = form.cleaned_data['sex'],
                age = form.cleaned_data['age'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
                disability_cate = form.cleaned_data['disability_cate'],
                job_interest = form.cleaned_data['job_interest'],
                job_exp = form.cleaned_data['job_exp'],
                expected_salary1 = expected_salary1,
                expected_salary2 = expected_salary2,
                expected_welfare = form.cleaned_data['expected_welfare'],
                talent = form.cleaned_data['talent'],
                talent2 = form.cleaned_data['talent2'],
                talent3 = form.cleaned_data['talent3'],
                more_resume = more_resume,
                province = form.cleaned_data['province'],
                get_more_info = form.cleaned_data['get_more_info'],
                )
            # messages.success(request, "สมัครบัญชีผู้ใช้สำเร็จแล้ว")
            # print(user.password)
            # user = authenticate(username=user.email,password=user.password)
            # login(request, user, backend='backends.email-auth.EmailBackend')
            return redirect('login')
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
            # login(request, user)
            my_group = Group.objects.get(name='company') 
            my_group.user_set.add(user)
            # p = Profile(picture = request.FILES['image'],user=user,name=username,email=email)
            # p.save()
            # login(request, user)
            return redirect('company_signup2', uid=user.id)
            # return redirect('company_signup2')
            # redirect process3
    else:
        form = CompanySignUpForm()
    return render(request, 'company_signup.html', {'form': form})


def company_signup2(request,uid):
    if request.method == 'POST':
        form = CompanyInformationForm(request.POST, request.FILES)
        if form.is_valid():
            print("Earn")
            user = User.objects.get(id=uid)
            profile = Profile.objects.create(user=user,profile_picture = request.FILES['company_image'],)
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
                hr_no=form.cleaned_data['hr_no'],
                )
            # user_auth = authenticate(username=user.email,password=user.password)
            # login(request, user_auth, backend='django.contrib.auth.backends.ModelBackend')
            # messages.success(request, "คุณได้สมัครบัญชีผู้ใช้สำเร็จแล้ว")

            return redirect('login')
            # redirect process3
    else:
        form = CompanyInformationForm()
    return render(request, 'company_signup2.html', {'form': form})

@login_required
def profile(request):
    list_noti = []
    read =True

    profile = Profile.objects.get(user=request.user)
    if User.objects.filter(pk=request.user.id, groups__name='disability').exists() :
        dis = DisabilityInfo.objects.get(profile=profile)
        noti = Notifications.objects.filter(tarket=profile)
       
   
        for i in noti:
            temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
            'job_name':"",'job_id':0,'noti_id':0}
            p = Profile.objects.get(user=i.user)
            dis = CompanyInfo.objects.get(profile=p)
            temp['job_name'] = i.job.title_th
            temp['job_id'] = i.job.id
            temp['name'] = dis.th_name
            temp['action'] = i.action
            temp['obj'] = i.obj
            temp['time'] = i.created_at
            temp['is_read'] = i.is_read
            temp['img'] = p.profile_picture.url
            temp['noti_id'] = i.id
                
            print(temp['is_read'])
            list_noti.append(temp)

        return render(request, 'profile.html',{'dis':dis,'noti':list_noti})
    else :
        
        return  redirect('company_profile')

@login_required
def edit_disable_profile(request):

    form = EditDisableProfileForm() 
    list_noti = []
    read =True
    profile = Profile.objects.get(user=request.user)
    if User.objects.filter(pk=request.user.id, groups__name='disability').exists() :
        dis = DisabilityInfo.objects.get(profile=profile)
        noti = Notifications.objects.filter(tarket=profile)
        form.fields['first_name'].widget.attrs['value'] = dis.first_name
        form.fields['last_name'].widget.attrs['value'] = dis.last_name
        form.fields['age'].widget.attrs['value'] = dis.age
        form.fields['address'].widget.attrs['value'] = dis.address
        form.fields['job_interest'].widget.attrs['value'] = dis.job_interest
        # form.fields['job_exp'].widget.attrs['placeholder'] = dis.job_exp
        form.fields['expected_welfare'].widget.attrs['value'] = dis.expected_welfare
        form.fields['expected_salary1'].widget.attrs['value'] = dis.expected_salary1
        form.fields['expected_salary2'].widget.attrs['value'] = dis.expected_salary2
        form.fields['phone_no'].widget.attrs['value'] = dis.phone_no
        form.fields['talent'].widget.attrs['value'] = dis.talent
        form.fields['talent2'].widget.attrs['value'] = dis.talent2
        form.fields['talent3'].widget.attrs['value'] = dis.talent3
        form.fields['province'].widget.attrs['value'] = dis.province
            
        for i in noti:
            temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
            'job_name':"",'job_id':0,'noti_id':0}
            p = Profile.objects.get(user=i.user)
            dis = CompanyInfo.objects.get(profile=p)
            temp['job_name'] = i.job.title_th
            temp['job_id'] = i.job.id
            temp['name'] = dis.th_name
            temp['action'] = i.action
            temp['obj'] = i.obj
            temp['time'] = i.created_at
            temp['is_read'] = i.is_read
            temp['img'] = p.profile_picture.url
            temp['noti_id'] = i.id
                
            print(temp['is_read'])
            list_noti.append(temp)

    if request.method == 'POST':
        form = EditDisableProfileForm(request.POST, request.FILES)
        if form.is_valid():
            expected_salary1 = 0 
            expected_salary2 = 0   
            if form.cleaned_data['expected_salary1'] >= form.cleaned_data['expected_salary2']:
                expected_salary1 = form.cleaned_data['expected_salary2']
                expected_salary2 = form.cleaned_data['expected_salary1']
            else:
                expected_salary1 = form.cleaned_data['expected_salary1']
                expected_salary2 = form.cleaned_data['expected_salary2']
            
            try:
                profile = Profile.objects.get(user=request.user)
                profile.profile_picture =  request.FILES['profile_image']
                profile.save()
            except Exception as e:
                pass
            disability = DisabilityInfo.objects.filter(profile=profile).update(
             
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                age = form.cleaned_data['age'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
                job_interest = form.cleaned_data['job_interest'],
                job_exp = form.cleaned_data['job_exp'],
                expected_salary1 = expected_salary1,
                expected_salary2 = expected_salary2,
                expected_welfare = form.cleaned_data['expected_welfare'],
                talent = form.cleaned_data['talent'],
                talent2 = form.cleaned_data['talent2'],
                talent3 = form.cleaned_data['talent3'],
                province = form.cleaned_data['province'],
              
              
                )
            return redirect('profile')

    # if User.objects.filter(pk=request.user.id, groups__name='disability').exists() :
    #     dis = DisabilityInfo.objects.get(profile=profile)
    #     noti = Notifications.objects.filter(tarket=profile)
            
    #     for i in noti:
    #         temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
    #         'job_name':"",'job_id':0,'noti_id':0}
    #         p = Profile.objects.get(user=i.user)
    #         dis = CompanyInfo.objects.get(profile=p)
    #         temp['job_name'] = i.job.title_th
    #         temp['job_id'] = i.job.id
    #         temp['name'] = dis.th_name
    #         temp['action'] = i.action
    #         temp['obj'] = i.obj
    #         temp['time'] = i.created_at
    #         temp['is_read'] = i.is_read
    #         temp['img'] = p.profile_picture.url
    #         temp['noti_id'] = i.id
                
    #         print(temp['is_read'])
    #         list_noti.append(temp)

    return render(request, 'edit_disable_profile.html',{'dis':dis,'form':form,'noti':list_noti})

@login_required
def edit_company_profile(request):
    form = EditCompanyProfileForm() 
    read =True
    list_noti = []
    profile = Profile.objects.get(user=request.user)
    company = CompanyInfo.objects.get(profile=profile)
    noti = Notifications.objects.filter(tarket=profile)
    form.fields['th_name'].widget.attrs['value'] = company.th_name
    form.fields['en_name'].widget.attrs['value'] = company.en_name
    # form.fields['info'].widget.attrs['value'] = company.info
    form.fields['address'].widget.attrs['value'] = company.address
    form.fields['website'].widget.attrs['value'] = company.website
    form.fields['company_type'].widget.attrs['value'] = company.company_type
    form.fields['fax'].widget.attrs['value'] = company.fax
    form.fields['hr_no'].widget.attrs['value'] = company.hr_no
    form.fields['phone_no'].widget.attrs['value'] = company.phone_no



    for i in noti:
        temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
        'job_name':"",'job_id':0,'noti_id':0,'job_interest':"",'disability_cate': '',
        'salary1':0,'salary2': 0,'province':'','job_exp':"",'dis_id':0}
        p = Profile.objects.get(user=i.user)
        dis = DisabilityInfo.objects.get(profile=p)
        temp['job_name'] = i.job.title_th
        temp['job_id'] = i.job.id
        temp['name'] = dis.first_name +" "+ dis.last_name
        temp['dis_id'] = dis.id
        temp['action'] = i.action
        temp['obj'] = i.obj
        temp['time'] = i.created_at
        temp['is_read'] = i.is_read
        temp['img'] = p.profile_picture.url
        temp['noti_id'] = i.id
        temp['salary1'] = dis.expected_salary1
        temp['salary2'] = dis.expected_salary2
        temp['province'] = dis.province
        temp['job_interest'] = dis.job_interest
        temp['job_exp'] = dis.job_exp
        temp['disability_cate'] = dis.disability_cate
        list_noti.append(temp)
    if request.method == 'POST':
        form = EditCompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                profile.profile_picture =  request.FILES['company_image']
                profile.save()
            except Exception as e:
                pass
            company = CompanyInfo.objects.filter(profile=profile).update(
                th_name=form.cleaned_data['th_name'],
                en_name=form.cleaned_data['en_name'],
                info = form.cleaned_data['info'],
                website = form.cleaned_data['website'],
                phone_no = form.cleaned_data['phone_no'],
                address = form.cleaned_data['address'],
                fax = form.cleaned_data['fax'],
                company_type = form.cleaned_data['company_type'],
                hr_no=form.cleaned_data['hr_no'],)
            return  redirect('company_profile')
             
    
    return render(request, 'edit_company_profile.html',{'form':form,'company':company,'noti':list_noti})  

@login_required
def company_profile(request):
    read =True
    list_noti = []
    profile = Profile.objects.get(user=request.user)
    company = CompanyInfo.objects.get(profile=profile)
    noti = Notifications.objects.filter(tarket=profile)
    for i in noti:
        temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
        'job_name':"",'job_id':0,'noti_id':0,'job_interest':"",'disability_cate': '',
        'salary1':0,'salary2': 0,'province':'','job_exp':"",'dis_id':0}
        p = Profile.objects.get(user=i.user)
        dis = DisabilityInfo.objects.get(profile=p)
        temp['job_name'] = i.job.title_th
        temp['job_id'] = i.job.id
        temp['name'] = dis.first_name +" "+ dis.last_name
        temp['dis_id'] = dis.id
        temp['action'] = i.action
        temp['obj'] = i.obj
        temp['time'] = i.created_at
        temp['is_read'] = i.is_read
        temp['img'] = p.profile_picture.url
        temp['noti_id'] = i.id
        temp['salary1'] = dis.expected_salary1
        temp['salary2'] = dis.expected_salary2
        temp['province'] = dis.province
        temp['job_interest'] = dis.job_interest
        temp['job_exp'] = dis.job_exp
        temp['disability_cate'] = dis.disability_cate
        list_noti.append(temp)

    
    return render(request, 'company_profile.html',{'company':company,'noti':list_noti})       



def profile_noti(request):
    list_noti = []
   
    profile = Profile.objects.get(user=request.user)
    noti = Notifications.objects.filter(tarket=profile)
    if User.objects.filter(pk=request.user.id, groups__name='disability').exists() :
        dis = DisabilityInfo.objects.get(profile=profile)
            
        for i in noti:
            temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
            'job_name':"",'job_id':0,'noti_id':0,'title_th':"",'disability_cate': '',
            'salary1':0,'salary2': 0,'province':'','detail':""}
            p = Profile.objects.get(user=i.user)
            comp = CompanyInfo.objects.get(profile=p)
            temp['job_name'] = i.job.title_th
            temp['job_id'] = i.job.id
            temp['name'] = comp.th_name
            temp['action'] = i.action
            temp['obj'] = i.obj
            temp['time'] = i.created_at
            temp['is_read'] = i.is_read
            temp['img'] = p.profile_picture.url
            temp['noti_id'] = i.id
            temp['salary1'] = i.job.salary1
            temp['salary2'] = i.job.salary2
            temp['province'] = i.job.province
            temp['detail'] = i.job.detail
            temp['disability_cate'] = i.job.disability_cate
                
            print(temp['is_read'])
            list_noti.append(temp)

        return render(request, 'profile_notifications.html',{'dis':dis,'noti':list_noti})
    else :
        comp = CompanyInfo.objects.get(profile=profile)
        for i in noti:
            temp = {'name': '', 'action': '', 'obj':'','time':None,'img':None,'is_read': False,
            'job_name':"",'job_id':0,'noti_id':0,'job_interest':"",'disability_cate': '',
            'salary1':0,'salary2': 0,'province':'','job_exp':"",'dis_id':0}
            p = Profile.objects.get(user=i.user)
            dis = DisabilityInfo.objects.get(profile=p)
            temp['job_name'] = i.job.title_th
            temp['job_id'] = i.job.id
            temp['name'] = dis.first_name +" "+ dis.last_name
            temp['dis_id'] = dis.id
            temp['action'] = i.action
            temp['obj'] = i.obj
            temp['time'] = i.created_at
            temp['is_read'] = i.is_read
            temp['img'] = p.profile_picture.url
            temp['noti_id'] = i.id
            temp['salary1'] = dis.expected_salary1
            temp['salary2'] = dis.expected_salary2
            temp['province'] = dis.province
            temp['job_interest'] = dis.job_interest
            temp['job_exp'] = dis.job_exp
            temp['disability_cate'] = dis.disability_cate

                
            list_noti.append(temp)
        return render(request, 'profile_comp_notifications.html',{'dis':comp,'noti':list_noti})
        
