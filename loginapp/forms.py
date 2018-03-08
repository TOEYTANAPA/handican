from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

# from myapp.models import Profile


class JobSignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
    	data = self.cleaned_data['email']
    	if User.objects.filter(email=data).exists():
        	raise forms.ValidationError("This email already used")
    	return data

    class Meta:
    
        model = User
        fields = (  'username','email', 'password1', 'password2', )
        exclude = ['username',]

class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data


    class Meta:
    
        model = User
        fields = ( 'email', 'password1', 'password2', )
        exclude = ['username',]

class JobInformationForm(forms.Form):
    
    GENDER_CHOICES = (
    ('ชาย', 'ชาย'),
    ('หญิง', 'หญิง')
    )
 
    SKILL_CHOICES = (

    ('เล็กน้อย', 'เล็กน้อย'),
    ('ปานกลาง', 'ปานกลาง'),
    ('ดี', 'ดี'),
    ('ดีมาก', 'ดีมาก'),
    )
    GRADUATE_CHOICES = (
    ('อ่านออก/เขียนได้', 'อ่านออก / เขียนได้'),
    ('อ่านออก/เขียนไม่ได', 'อ่านออก / เขียนไม่ได'),
    ('ต่ำกว่า ป.4', 'ต่ำกว่า ป.4'),
    ('ป.4', 'ป.4'),
    ('ป.6', 'ป.6'),
    ('ปวช.', 'ปวช.'),
    ('ปวส.', 'ปวส.'),
    ('อนุปริญญา', 'อนุปริญญา'),
    ('ปริญญาตรี', 'ปริญญาตรี'),
    ('สูงปริญญาตรี', 'สูงปริญญาตรี'),
    ('อื่นๆ', 'อื่นๆ'),
    )

    STATUS_CHOICES= (
    ('ว่างงาน', 'ว่างงาน'),
    ('รองาน', 'รองาน'),
    ('เปลี่ยนงาน', 'เปลี่ยนงาน'),
    )
    WORKING_TIME_CHOICES= (
    ('กลางวัน', 'กลางวัน'),
    ('กลางคืน', 'กลางคืน'),
    ('Part-time', 'Part-time'),
    )
    OTHER_PROVINCE_CHOICES= (
    (True, 'ได้'),
    (False, 'ไม่ได้'),
    )
    TRAVELING_BY_MYSELF_CHOICES= (
    (True, 'ได้'),
    (False, 'ไม่ได้'),
    )
    TRUE_FALSE_CHOICES= (
    (True, 'ได้'),
    (False, 'ไม่ได้'),
    )
    HAVE_CHOICES= (
    (True, 'มี'),
    (False, 'ไม่มี'),
    )
    DIS_CATE_CHOICES= (
    ('ทางการมองเห็น', 'ทางการมองเห็น'),
    ('ทางการได้ยินหรือการสื่อความหมาย', 'ทางการได้ยินหรือการสื่อความหมาย'),
    ('ทางกายหรือการเคลื่อนไหว', 'ทางกายหรือการเคลื่อนไหว'),
    
    )
    DIS_LEVEL_CHOICES= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    
    )   
    DIS_REASON_CHOICES= (
   
    ('แต่กำเนิด', 'แต่กำเนิด'),
    ('อุบัติเหตุ', 'อุบัติเหตุ'),
    ('อื่นๆ', 'อื่นๆ'),
  
    )
    DIS_EQUIP_CHOICES= (
   
    ('รถเข็น', 'รถเข็น'),
    ('ไม้ค้ำยัน', 'ไม้ค้ำยัน'),
    ('เบรส (พยุงขา)', 'เบรส (พยุงขา)'),
    ('เบรสและไม้ค้ำยัน', 'เบรสและไม้ค้ำยัน'),
    ('ไม้เท้าขาว (ตาบอด)', 'ไม้เท้าขาว (ตาบอด)'),
    ('แขนเทียม', 'แขนเทียม'),
    ('ขาเทียม', 'ขาเทียม'),
    ('แขนเทียมและขาเทียม', 'แขนเทียมและขาเทียม'),
    ('เครื่องช่วยฟัง', 'เครื่องช่วยฟัง'),
    ('อื่นๆ', 'อื่นๆ'),
    ('ไม่มี', 'ไม่มี'),

  
    )
    SARALY_CHOICES =(
    ('ไม่ระบุ','ไม่ระบุ'),
    ('น้อยกว่า 10,000','น้อยกว่า 10,000' ),
    ('10,000-19,000','10,000-19,000'),
    ('20,000-29,999','20,000-29,999'),
    ('30,000-39,000','30,000-39,000'),
    ('40,000-49,000','40,000-49,000'),
    ('50,000 ขึ้นไป','50,000 ขึ้นไป')
    )
    
    PROVINCE_CHOICES= (
    ('กรุงเทพมหานคร', 'กรุงเทพมหานคร'),
    ('กระบี่', 'กระบี่'),
    ('กาญจนบุรี', 'กาญจนบุรี'),
    ('กาฬสินธุ์', 'กาฬสินธุ์'),
    ('กำแพงเพชร', 'กำแพงเพชร'),
    ('ขอนแก่น', 'ขอนแก่น'),
    ('จันทบุรี', 'จันทบุรี'),
    ('ฉะเชิงเทรา', 'ฉะเชิงเทรา'),
    ('ชัยนาท', 'ชัยนาท'),
    ('ชัยภูมิ', 'ชัยภูมิ'),
    ('ชุมพร', 'ชุมพร'),
    ('ชลบุรี', 'ชลบุรี'),
    ('เชียงใหม่', 'เชียงใหม่'),
    ('เชียงราย', 'เชียงราย'),
    ('ตรัง', 'ตรัง'),
    ('ตราด', 'ตราด'),
    ('ตาก', 'ตาก'),
    ('นครนายก', 'นครนายก'),
    ('นครปฐม', 'นครปฐม'),
    ('นครพนม', 'นครพนม'),
    ('นครราชสีมา', 'นครราชสีมา'),
    ('นครศรีธรรมราช', 'นครศรีธรรมราช'),
    ('นครสวรรค์', 'นครสวรรค์'),
    ('นราธิวาส', 'นราธิวาส'),
    ('น่าน', 'น่าน'),
    ('นนทบุรี', 'นนทบุรี'),
    ('บึงกาฬ', 'บึงกาฬ'),
    ('บุรีรัมย์', 'บุรีรัมย์'),
    ('ประจวบคีรีขันธ์', 'ประจวบคีรีขันธ์'),
    ('ปทุมธานี', 'ปทุมธานี'),
    ('ปราจีนบุรี', 'ปราจีนบุรี'),
    ('ปัตตานี', 'ปัตตานี'),
    ('พะเยา', 'พะเยา'),
    ('พระนครศรีอยุธยา', 'พระนครศรีอยุธยา'),
    ('พังงา', 'พังงา'),
    ('พิจิตร', 'พิจิตร'),
    ('พิษณุโลก', 'พิษณุโลก'),
    ('เพชรบุรี', 'เพชรบุรี'),
    ('เพชรบูรณ์', 'เพชรบูรณ์'),
    ('แพร่', 'แพร่'),
    ('พัทลุง', 'พัทลุง'),
    ('ภูเก็ต', 'ภูเก็ต'),
    ('มหาสารคาม', 'มหาสารคาม'),
    ('มุกดาหาร', 'มุกดาหาร'),
    ('แม่ฮ่องสอน', 'แม่ฮ่องสอน'),
    ('ยโสธร', 'ยโสธร'),
    ('ยะลา', 'ยะลา'),
    ('ร้อยเอ็ด', 'ร้อยเอ็ด'),
    ('ระนอง', 'ระนอง'),
    ('ระยอง', 'ระยอง'),
    ('ราชบุรี', 'ราชบุรี'),
    ('ลพบุรี', 'ลพบุรี'),
    ('ลำปาง', 'ลำปาง'),
    ('ลำพูน', 'ลำพูน'),
    ('เลย', 'เลย'),
    ('ศรีสะเกษ', 'ศรีสะเกษ'),
    ('สกลนคร', 'สกลนคร'),
    ('สงขลา', 'สงขลา'),
    ('สมุทรสาคร', 'สมุทรสาคร'),
    ('สมุทรปราการ', 'สมุทรปราการ'),
    ('สมุทรสงคราม', 'สมุทรสงคราม'),
    ('สระแก้ว', 'สระแก้ว'),
    ('สระบุรี', 'สระบุรี'),
    ('สิงห์บุรี', 'สิงห์บุรี'),
    ('สุโขทัย', 'สุโขทัย'),
    ('สุพรรณบุรี', 'สุพรรณบุรี'),
    ('สุราษฎร์ธานี', 'สุราษฎร์ธานี'),
    ('สุรินทร์', 'สุรินทร์'),
    ('สตูล', 'สตูล'),
    ('หนองคาย', 'หนองคาย'),
    ('หนองบัวลำภู', 'หนองบัวลำภู'),
    ('อำนาจเจริญ', 'อำนาจเจริญ'),
    ('อุดรธานี', 'อุดรธานี'),
    ('อุตรดิตถ์', 'อุตรดิตถ์'),
    ('อุทัยธานี', 'อุทัยธานี'),
    ('อุบลราชธานี', 'อุบลราชธานี'),
    ('อ่างทอง', 'อ่างทอง'),
    ('อื่นๆ', 'อื่นๆ'),
    
    )
    YEARS= [str(x) for x in range(1940,datetime.datetime.now().year+1)]
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    disable_id =  forms.CharField(max_length=20, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    first_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    last_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    age =  forms.IntegerField( help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    sex = forms.ChoiceField(choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
    phone_no =  forms.CharField(max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    citizen_id = forms.CharField(max_length=15, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    region = forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
    # address
    registration_address  =   forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 4,'class': 'uk-textarea', }))
    current_address = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 4,'class': 'uk-textarea', }))
    registration_province =  forms.ChoiceField(choices = PROVINCE_CHOICES, label="",initial='',
     widget=forms.Select(attrs={'class': ' uk-select '}))
    current_province =  forms.ChoiceField(choices = PROVINCE_CHOICES, label="",initial='',
     widget=forms.Select(attrs={'class': ' uk-select '}))

    # birthdate
    birth_date= forms.DateField(label='', initial=datetime.datetime.now(),
     widget=forms.SelectDateWidget(years=YEARS,attrs={'class': ' uk-select '}))
    
    # graduate
    graduate = forms.ChoiceField(choices = GRADUATE_CHOICES,  label="",initial='',
     widget=forms.Select(attrs={'class': 'uk-select'}))
    graduate_year = forms.ChoiceField(choices = YEAR_CHOICES,initial=datetime.datetime.now().year, label="",
     widget=forms.Select(attrs={'class': 'uk-select'}))
    educational_institution = forms.CharField(max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    faculty = forms.CharField(max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    branch =  forms.CharField(max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    honor_name =  forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    honor_year =  forms.ChoiceField(required=False,choices = YEAR_CHOICES,initial=datetime.datetime.now().year, label="",
     widget=forms.Select(attrs={'class': 'uk-select'}))
    agency_honor = forms.CharField(required=False,max_length=500, help_text='',
        widget=forms.TextInput(attrs={'class': 'uk-input'}))
    hobbies = forms.CharField(max_length=2500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    interesting_work_cate = forms.CharField(max_length=2500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    

    # last company
    job_exp = forms.ChoiceField(choices = HAVE_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select','id':"job_exp"}))
    last_company_name = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    last_company_province = forms.ChoiceField(required=False,choices = PROVINCE_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    
    position = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    working_start_date =forms.DateField(required=False,label='', initial=datetime.datetime.now(),
     widget=forms.SelectDateWidget(years=YEARS,attrs={'class': ' uk-select '}))
    working_end_date =forms.DateField(required=False,label='', initial=datetime.datetime.now(),
     widget=forms.SelectDateWidget(years=YEARS,attrs={'class': ' uk-select '}))
    quit_job_reason=forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
    # quality additional skll
    language1 = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    listen_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    speaking_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    reading_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    writing_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    language2 = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    listen_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    speaking_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    reading_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    writing_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    language3 = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    listen_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    speaking_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    reading_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    writing_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    language4 = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    listen_skill4 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    speaking_skill4 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    reading_skill4 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    writing_skill4 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    computer_skill1 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill2 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill3 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill4 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill5 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
    level_computer_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill4 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill5 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))


    # computer skill
    
    # working
    helping_myself = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="",initial='', 
        widget=forms.RadioSelect(attrs={}))
    traveling_by_myself = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="",initial='', 
        widget=forms.RadioSelect(attrs={}))
    work_in_other_province = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="",initial='', 
        widget=forms.RadioSelect(attrs={}))
    working_time = forms.ChoiceField(choices = WORKING_TIME_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    current_status = forms.ChoiceField(choices = STATUS_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    
    # disable category
    disability_cate = forms.ChoiceField(choices = DIS_CATE_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select','id':'disability_cate'}))
    disability_level = forms.ChoiceField(choices = DIS_LEVEL_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    disability_reason = forms.ChoiceField(choices = DIS_REASON_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    disabled_year = forms.ChoiceField(choices = YEAR_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    disabled_equiptment = forms.ChoiceField(choices = DIS_EQUIP_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    # 
    
  

    # disease
    congenital_disease =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # law
    lawsuit = forms.ChoiceField(choices = HAVE_CHOICES, label="",initial='', 
        widget=forms.RadioSelect(attrs={}))


    job_interest1 =  forms.CharField(required=False,max_length=2000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'})) 
    job_interest2 =  forms.CharField(required=False,max_length=2000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'})) 
    job_interest3 =  forms.CharField(required=False,max_length=2000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'})) 
    expected_salary1 =  forms.ChoiceField(choices = SARALY_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'})) 
    expected_salary2 =  forms.ChoiceField(choices = SARALY_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    expected_salary3 =  forms.ChoiceField(choices = SARALY_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))

    expected_welfare =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
   

    
    # address =   forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
    # talent =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # talent2 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # talent3 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # more_resume = forms.FileField(required=False,)
    profile_image = forms.FileField()
    # get_more_info = forms.BooleanField(required=False,initial=False)

class CompanyInformationForm(forms.Form):
    

    th_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    en_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    address =  forms.CharField(max_length=5000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    info =  forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
    website =  forms.CharField(max_length=50,required=False, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    phone_no =  forms.CharField(max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    hr_no =  forms.CharField(max_length=13,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'})) 
    fax = forms.CharField(max_length=30,required=False, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    company_type =  forms.CharField(max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    company_image = forms.FileField()
    get_more_info = forms.BooleanField(required=False,initial=False)


class EditDisableProfileForm(forms.Form):
    first_name =  forms.CharField(required=False,max_length=100, help_text='',
        widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium '}))
    last_name =  forms.CharField(required=False,max_length=100, help_text='',
        widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium '}))
    age =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-small'}))

    address =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input '}))
    job_interest =  forms.CharField(required=False,max_length=2000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'})) 
    job_exp =  forms.CharField(required=False,max_length=5000, help_text='',
        widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea','id':'myTextArea' }))
    expected_salary1 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-small','type':'number'}))
    expected_salary2 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-small','type':'number'}))
    phone_no =  forms.CharField(required=False,max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    expected_welfare =  forms.CharField(required=False,max_length=1000, help_text='',
        widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium',}))
    talent =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    talent2 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    talent3 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    profile_image = forms.FileField(required=False)
    province =  forms.CharField(required=False,max_length=250, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))

class EditCompanyProfileForm(forms.Form):

    th_name =  forms.CharField(required=False,max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    en_name =  forms.CharField(required=False,max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    address =  forms.CharField(required=False,max_length=5000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    info =  forms.CharField(required=False,max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
    website =  forms.CharField(required=False,max_length=50, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input  uk-form-width-medium'}))
    phone_no =  forms.CharField(required=False,max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    hr_no =  forms.CharField(required=False,max_length=13,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'})) 
    fax = forms.CharField(required=False,max_length=30, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    company_type =  forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))
    company_image = forms.FileField(required=False)
    # province =  forms.CharField(required=False,max_length=250, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input uk-form-width-medium'}))



# class UserCreationForm(forms.ModelForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#     password1 = forms.CharField(label=_("Password"),
#         widget=forms.PasswordInput)
#     password2 = forms.CharField(label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         help_text=_("Enter the same password as above, for verification."))

#     class Meta:
#         model = User
#         fields = ("username",)

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
