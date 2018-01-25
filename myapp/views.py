from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate,update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,Http404
from myapp.models import *
from django.views.generic.edit import UpdateView
from django.db.models import Q
import difflib

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

    


def disable_detail(request,dis_id):
    dis = DisabilityInfo.objects.get(id=dis_id)
    status = "ยังไม่ส่งคำเชิญ"
    try :
        status = InviteProcess.objects.get(disability=dis,job__id=3)
        status = status.status

    except :
        pass

    return render(request, 'disable_detail.html', {'dis':dis,'status':status,'job_id':3})

def invite_job_to_disability(request,dis_id,job_id):
    tarket = DisabilityInfo.objects.get(id=dis_id)
    
  
    job = Job.objects.get(id=job_id)
    Notifications.objects.create(user=request.user,job=job,tarket=tarket.profile,
        action="ส่งคำเชิญ",obj="สมัครงาน")

    status = InviteProcess.objects.create(disability=tarket,status="ส่งคำเชิญ",job=job)

    # status = 0
    # try :
    #     temp = statusDisability.objects.get(disability=tarket,job=job)
    #     if temp.status == "ยังไม่ส่งคำเชิญ" :
    #         status = 0
    #     elif temp.status == "ส่งคำเชิญ" :
    #         status = 2
    #     elif temp.status == "ตอบรับคำเชิญ" :


    return render(request, 'disable_detail.html', {'dis':tarket,'status':status.status,'job_id':job.id})

def job_detail(request,job_name,job_id):
    # comp = CompanyInfo.objects.get(profile__user= request.user)

    job = Job.objects.get(title_th=job_name,id=job_id)
    processing = False

    
    if User.objects.filter(pk=request.user.id, groups__name='disability').exists() :
        try :

            profile = Profile.objects.get(user=request.user)
            dis = DisabilityInfo.objects.get(profile=profile)
            o = InviteProcess.objects.all()
        
            for i in o :
                print(i.status)
                print(i.disability)
                print(i.job)
                print(job)
            try :
                InviteProcess.objects.get(disability=dis,status="ส่งคำเชิญ",job=job)
                processing = True
            except :
                raise



   
        except :
            raise

    return render(request, 'job_detail.html', {'job':job,'process':processing})

def click_noti(request,job_name,job_id,noti_id):
    noti = Notifications.objects.filter(id=noti_id).update(is_read=True)
    print("Delete")
    

    


    return job_detail(request,job_name,job_id)

def confirm_job(request,job_name,job_id):
    job = Job.objects.get(title_th=job_name,id=job_id)
    ConfirmJob.objects.create(user=request.user,job=job)
    return render(request, 'job_detail.html', {'job':job,'status':1})


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

@login_required
def search(request):
    return render(request, 'search.html',{})
  
@login_required
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
            else :
                age1 = form.cleaned_data['age1']
                age2 = form.cleaned_data['age2']

            if form.cleaned_data['salary1'] >= form.cleaned_data['salary2'] :
                salary2 = form.cleaned_data['salary1']
                salary1 = form.cleaned_data['salary2']
            else :
                salary1 = form.cleaned_data['salary1']
                salary2 = form.cleaned_data['salary2']
                
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
        temp_dict = {}
       
        company = CompanyInfo.objects.get(profile__user=request.user)
        job_declared = Job.objects.filter(company=company)
        job_title_th = ""
        for j in job_declared:
            job_title_th = j.title_th
            break

        job_required = Job.objects.get(title_th=job_title_th) 
        dis_list = DisabilityInfo.objects.all()
        print(dis_list)

        south = ['จังหวัดกระบี่','จังหวัดชุมพร', 'จังหวัดตรัง', 'จังหวัดนครศรีธรรมราช' ,'จังหวัดนราธิวาส',
        'จังหวัดปัตตานี', 'จังหวัดพังงา', 'จังหวัดพัทลุง','จังหวัดภูเก็ต' ,'จังหวัดยะลา' ,'จังหวัดระนอง' ,
        'จังหวัดสงขลา', 'จังหวัดสตูล', 'จังหวัดสุราษฎร์ธานี']
        east = ['จังหวัดจันทบุรี', 'จังหวัดฉะเชิงเทรา' ,'จังหวัดชลบุรี' ,'จังหวัดตราด', 'จังหวัดปราจีนบุรี', 'จังหวัดระยอง' ,'จังหวัดสระแก้ว']
        west = ['จังหวัดกาญจนบุรี', 'จังหวัดตาก' ,'จังหวัดประจวบคีรีขันธ์','จังหวัดเพชรบุรี', 'จังหวัดราชบุรี']
        north = ['จังหวัดเชียงราย', 'จังหวัดเชียงใหม่' ,'จังหวัดน่าน', 'จังหวัดพะเยา', 'จังหวัดแพร่' ,'จังหวัดแม่ฮ่องสอน' ,'จังหวัดลำปาง', 'จังหวัดลำพูน', 'จังหวัดอุตรดิตถ์']
        north_east = ['กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ' ,'นครพนม' ,'นครราชสีมา' ,'บุรีรัมย์' ,'มหาสารคาม', 'มุกดาหาร',
        'ยโสธร', 'ร้อยเอ็ด','เลย', 'ศรีสะเกษ','สกลนคร' ,'สุรินทร์' ,'หนองคาย' ,'หนองบัวลำภู' ,'อำนาจเจริญ' ,
        'อุดรธานี','อุบลราชธานี' , 'บึงกาฬ']
        central = ['กรุงเทพมหานคร' ,'กำแพงเพชร', 'ชัยนาท' ,'นครนายก' ,'นครปฐม' ,'นครสวรรค์', 'นนทบุรี', 
        'ปทุมธานี', 'พระนครศรีอยุธยา' ,'พิจิตร' ,'พิษณุโลก','เพชรบูรณ์', 'ลพบุรี' ,'สมุทรปราการ', 'สมุทรสงคราม' ,
        'สมุทรสาคร' ,'สระบุรี' ,'สิงห์บุรี', 'สุโขทัย','สุพรรณบุรี', 'อ่างทอง', 'อุทัยธานี']

        for d in dis_list:
            score = 0
            zone = ""
            dis_zone = ""
            # lower_north_central_top = "สุโขทัย"
            founded_province = False 
            the_string = d.job_interest
            j_split = the_string.split(",")

            if d.disability_cate in job_required.disability_cate:
                score +=20
            if d.province in job_required.province:
                score += 20
            else:
                if job_required.province in north:
                    zone = "ภาคเหนือ"
                elif job_required.province in north_east:
                    zone = "ภาคตะวันออกเฉียงเหนือ"
                elif job_required.province in central:
                    zone = "ภาคกลาง"
                elif job_required.province in east:
                    zone = "ภาคตะวันออก"
                elif job_required.province in west:
                    zone = "ภาคตะวันตก"           

                if d.province in north:
                    dis_zone = "ภาคเหนือ"
                elif d.province in north_east:
                    dis_zone = "ภาคตะวันออกเฉียงเหนือ"
                elif d.province in central:
                    dis_zone = "ภาคกลาง"
                elif d.province in east:
                    dis_zone = "ภาคตะวันออก"
                elif d.province in west:
                    dis_zone = "ภาคตะวันตก" 
                if zone == dis_zone:
                    score +=10
            for jl in j_split:
                
                seq = difflib.SequenceMatcher(None,job_required.title_th,jl)
                percen = seq.ratio()*100
                print("percen ",percen)
                if percen >= 30.0:
                    score += 20
                elif percen>=10.0 and percen <=29.0:
                    score += 10
                elif percen < 10.0:
                    score+=0   
           

            if d.expected_salary1 <= job_required.salary1 or d.expected_salary1 <= job_required.salary2 :
                if d.expected_salary2 <= job_required.salary2:
                    score +=20
                elif d.expected_salary2 > job_required.salary2  :
                    score +=15
                else:
                    score +=15
                     

            if d.age >= job_required.age1 and d.age <= job_required.age2 :
                score +=20
            elif  d.age >= job_required.age1 and d.age >= job_required.age2 :
                score +=5
            elif  d.age <= job_required.age1 :
                score +=5

            # print (score)
            temp_dict[d.id] = score
        output_match = []
        temp_dict_reverse = sorted(temp_dict, key=temp_dict.get, reverse=True)
        print("temp_dict_reverse",temp_dict_reverse)   
        for r in temp_dict_reverse:
            temp={"name":"","job_interest":"","url_pic":None,"expected_salary1":0,"expected_salary2":0,
            "job_exp":"","dis_cate":"","province":"","score":0}
            dis = DisabilityInfo.objects.get(id=r)

            temp['score'] = temp_dict[r]
            temp['name'] = dis.first_name+" "+dis.last_name
            temp['job_interest'] = dis.job_interest
            temp['expected_salary1'] = dis.expected_salary1
            temp['expected_salary2'] = dis.expected_salary2
            temp['job_exp'] = dis.job_exp
            temp['dis_cate'] = dis.disability_cate
            temp['province'] = dis.province
            temp['url_pic'] = Profile.objects.get(id=dis.profile.id).profile_picture.url
            output_match.append(temp)
        # print (output)
            # output_match.append(temp)
        print (output_match)
        form = CreateJobForm()

    return render(request, 'employer_search.html',{'form':form,'job_declared':job_declared,'output':output_match})


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
  
@login_required
def employer_search_disability(request):
    company = CompanyInfo.objects.get(profile__user=request.user)
    job_declared = Job.objects.filter(company=company)
    if request.method == 'POST':
        job_title_th = request.POST['selectJob']
        # job_title_th = "เว็บคอร์สแบงก์ค็อก2 นักออกแบบบ้าน"
        temp_dict = {}
        temp_dict2 = {}
        print("aaaaaaaaaaaaaaaaaaaa",job_title_th)
        # company = CompanyInfo.objects.get(profile__user=request.user)
        # if request.is_ajax():
        #     address = request.GET.get('address',False)
        #     phone_number = request.GET.get('phone_number',False)
        job_required = Job.objects.get(title_th=job_title_th) 
        dis_list = DisabilityInfo.objects.all()
        print(dis_list)

        south = ['จังหวัดกระบี่','จังหวัดชุมพร', 'จังหวัดตรัง', 'จังหวัดนครศรีธรรมราช' ,'จังหวัดนราธิวาส',
        'จังหวัดปัตตานี', 'จังหวัดพังงา', 'จังหวัดพัทลุง','จังหวัดภูเก็ต' ,'จังหวัดยะลา' ,'จังหวัดระนอง' ,
        'จังหวัดสงขลา', 'จังหวัดสตูล', 'จังหวัดสุราษฎร์ธานี']
        east = ['จังหวัดจันทบุรี', 'จังหวัดฉะเชิงเทรา' ,'จังหวัดชลบุรี' ,'จังหวัดตราด', 'จังหวัดปราจีนบุรี', 'จังหวัดระยอง' ,'จังหวัดสระแก้ว']
        west = ['จังหวัดกาญจนบุรี', 'จังหวัดตาก' ,'จังหวัดประจวบคีรีขันธ์','จังหวัดเพชรบุรี', 'จังหวัดราชบุรี']
        north = ['จังหวัดเชียงราย', 'จังหวัดเชียงใหม่' ,'จังหวัดน่าน', 'จังหวัดพะเยา', 'จังหวัดแพร่' ,'จังหวัดแม่ฮ่องสอน' ,'จังหวัดลำปาง', 'จังหวัดลำพูน', 'จังหวัดอุตรดิตถ์']
        north_east = ['กาฬสินธุ์', 'ขอนแก่น', 'ชัยภูมิ' ,'นครพนม' ,'นครราชสีมา' ,'บุรีรัมย์' ,'มหาสารคาม', 'มุกดาหาร',
        'ยโสธร', 'ร้อยเอ็ด','เลย', 'ศรีสะเกษ','สกลนคร' ,'สุรินทร์' ,'หนองคาย' ,'หนองบัวลำภู' ,'อำนาจเจริญ' ,
        'อุดรธานี','อุบลราชธานี' , 'บึงกาฬ']
        central = ['กรุงเทพมหานคร' ,'กำแพงเพชร', 'ชัยนาท' ,'นครนายก' ,'นครปฐม' ,'นครสวรรค์', 'นนทบุรี', 
        'ปทุมธานี', 'พระนครศรีอยุธยา' ,'พิจิตร' ,'พิษณุโลก','เพชรบูรณ์', 'ลพบุรี' ,'สมุทรปราการ', 'สมุทรสงคราม' ,
        'สมุทรสาคร' ,'สระบุรี' ,'สิงห์บุรี', 'สุโขทัย','สุพรรณบุรี', 'อ่างทอง', 'อุทัยธานี']

        for d in dis_list:
            score = 0
            zone = ""
            dis_zone = ""
            # lower_north_central_top = "สุโขทัย"
            founded_province = False 
            the_string = d.job_interest
            j_split = the_string.split(",")

            if d.disability_cate in job_required.disability_cate:
                score +=20
            if d.province in job_required.province:
                score += 20
            else:
                if job_required.province in north:
                    zone = "ภาคเหนือ"
                elif job_required.province in north_east:
                    zone = "ภาคตะวันออกเฉียงเหนือ"
                elif job_required.province in central:
                    zone = "ภาคกลาง"
                elif job_required.province in east:
                    zone = "ภาคตะวันออก"
                elif job_required.province in west:
                    zone = "ภาคตะวันตก"           

                if d.province in north:
                    dis_zone = "ภาคเหนือ"
                elif d.province in north_east:
                    dis_zone = "ภาคตะวันออกเฉียงเหนือ"
                elif d.province in central:
                    dis_zone = "ภาคกลาง"
                elif d.province in east:
                    dis_zone = "ภาคตะวันออก"
                elif d.province in west:
                    dis_zone = "ภาคตะวันตก" 
                if zone == dis_zone:
                    score +=10
            for jl in j_split:
                
                seq = difflib.SequenceMatcher(None,job_required.title_th,jl)
                percen = seq.ratio()*100
                print("percen ",percen)
                if percen >= 30.0:
                    score += 20
                elif percen>=10.0 and percen <=29.0:
                    score += 10
                elif percen < 10.0:
                    score+=0   
           

            if d.expected_salary1 <= job_required.salary1 or d.expected_salary1 <= job_required.salary2 :
                if d.expected_salary2 <= job_required.salary2:
                    score +=20
                elif d.expected_salary2 > job_required.salary2:
                    score +=15
                else:
                    score +=15 

            if d.age >= job_required.age1 and d.age <= job_required.age2 :
                score +=20
            elif  d.age >= job_required.age1 and d.age >= job_required.age2 :
                score +=5
            elif  d.age <= job_required.age1 :
                score +=5

            # print (score)
            temp_dict[d.id] = score
        output = []
        temp_dict_reverse = sorted(temp_dict, key=temp_dict.get, reverse=True)
        # print("temp_dict_reverse",temp_dict_reverse)   
        for r in temp_dict_reverse:
            temp={"name":"","job_interest":"","url_pic":None,"expected_salary1":0,"expected_salary2":0,
            "job_exp":"","dis_cate":"","province":"","score":0}
            dis = DisabilityInfo.objects.get(id=r)

            temp['score'] = temp_dict[r]
            temp['name'] = dis.first_name+" "+dis.last_name
            temp['job_interest'] = dis.job_interest
            temp['expected_salary1'] = dis.expected_salary1
            temp['expected_salary2'] = dis.expected_salary2
            temp['job_exp'] = dis.job_exp
            temp['dis_cate'] = dis.disability_cate
            temp['province'] = dis.province
            temp['url_pic'] = Profile.objects.get(id=dis.profile.id).profile_picture.url
            output.append(temp)
        # print (output)
        return render(request, 'employer_search.html',{'output':output,'job_declared':job_declared,'job_title_th':job_title_th})

    # return render(request, 'employer_search.html',)
    # print("temp_dict2",temp_dict2)
    # for key, value in temp_dict2.items():
    #     print ("key "+str(key)+" value "+str(value))

  
            # if d.province in north:



            # for pn in north:
            #     if d.province in pn:
            #         founded_province = True
            #         score +=20
            #         break
            # if not founded_province:
            #     for ps in south:
            #         pass
            
            # for pe in east:
            #     pass
            
            # pak
       

     

    # print("s1 ",job_required.salary1)

    # disability_list = DisabilityInfo.objects.filter(
    # Q(province__icontains=job_required.province),
    # Q(disability_cate__icontains=job_required.disability_cate),
    # Q(job_interest__icontains=job_required.qulification),
    # Q(expected_salary1__gte=job_required.salary1) | Q(expected_salary1__lte=job_required.salary2) & Q(expected_salary2__lte=job_required.salary2),
    # )

    # # dis_list = DisabilityInfo.objects.filter(address__icontains=job_required.traveling)
    # dis_list = DisabilityInfo.objects.filter(address__icontains=job_required.traveling)

    # for dis in disability_list:
    #     print(dis.expected_salary1)
    #     print(dis.expected_salary2)
    # print(job_required)
    # pass


    # def create_job(request):
    # if request.method == 'POST':
    #     form = CreateJobForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         company = CompanyInfo.objects.get(profile__user=request.user)
    #         cj = Job.objects.create(
    #             company =company,
    #             title_th=form.cleaned_data['title_th'],
    #             title_en=form.cleaned_data['title_en'],
    #             age = form.cleaned_data['age'],
    #             sex = form.cleaned_data['sex'],
    #             detail = form.cleaned_data['job_detail'],
    #             disability_cate = form.cleaned_data['disability_type'],
    #             traveling = form.cleaned_data['traveling'],
    #             welfare = form.cleaned_data['welfare'],
    #             salary = form.cleaned_data['salary'],
    #             company_image =request.FILES['company_image'],
           
    #             )
        
    #         messages.success(request, "คุณได้สมัครบัญชีผู้ใช้สำเร็จแล้ว")
    #         redirect('employer_search')


    # else :
    #     form = CreateJobForm()
    # return render(request, 'create_job.html',{'form':form})

