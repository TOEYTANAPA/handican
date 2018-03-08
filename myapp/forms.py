from django import forms
import datetime
from django.contrib.admin.widgets import AdminTimeWidget
from django.utils.safestring import mark_safe
# from .select_time_widget import SelectTimeWidget
# from django.forms.widgets import SelectDateWidget, SelectTimeWidget
# from datetime import datetime
# from django.contrib.auth.models import User
# from myapp.models import Profile
from ckeditor.fields import RichTextFormField



class ContactForm(forms.Form):
    name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    email =  forms.EmailField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    phone =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    subject =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    message =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
   
# class TimePickerWidget(forms.TimeInput):                                                  
#     def render(self, name, value, attrs=None):                                                
#         htmlString = u''                                                                      
#         htmlString += u'<select name="%s">' % (name)                                          
#         for i in range(12):                                                                   
#                 htmlString += ('<option value="%d:00 AM">%d:00 AM</option>' % (i,i))          
#         htmlString +='</select>'                                                              
#         return mark_safe(u''.join(htmlString))    

class CreateJobForm(forms.Form):

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
    SKILL_CHOICES = (
    ('เล็กน้อย', 'เล็กน้อย'),
    ('ปานกลาง', 'ปานกลาง'),
    ('ดี', 'ดี'),
    ('ดีมาก', 'ดีมาก'),
    )
    GENDER_CHOICES = (
    ('ชาย', 'ชาย'),
    ('หญิง', 'หญิง'),
    ('หญิง, ชาย', 'หญิง, ชาย')
    )
    WORKING_TIME_CHOICES= (
    ('กลางวัน', 'กลางวัน'),
    ('กลางคืน', 'กลางคืน'),
    ('Part-time', 'Part-time'),
    )
    SARALY_CHOICES =(
    ('น้อยกว่า 10,000','น้อยกว่า 10,000' ),
    ('10,000-19,000','10,000-19,000'),
    ('20,000-29,000','20,000-29,000'),
    ('30,000-39,000','30,000-39,000'),
    ('40,000-49,000','40,000-49,000'),
    ('50,000 ขึ้นไป','50,000 ขึ้นไป')
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
        # times = [] 
        # times.append(( time() + timedelta(minutes=15) * i).time().strftime("%I:%M %p").lstrip('0'))
        
        # TIMES_CHOICES =[( choice.strftime("%H:%M:%S"), choice.strftime("%I:%M %p").lstrip('0') ) for choice in times]
    title_th =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    title_en =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    age1 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
    age2 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
    email =  forms.EmailField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    sex = forms.ChoiceField(required=False,choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
    phone_no =  forms.CharField(max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # job_detail = RichTextFormField()
    job_detail = forms.CharField(required=False,max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows':5,'class': 'uk-textarea', }))
  
    salary =  forms.ChoiceField(choices = SARALY_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    location = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
    province =  forms.ChoiceField(choices = PROVINCE_CHOICES, label="",initial='',
     widget=forms.Select(attrs={'class': ' uk-select '}))
    language = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # listen_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    # speaking_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    # reading_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    # writing_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    # listen_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', 
    #     widget=forms.RadioSelect(attrs={}))    
    # speaking_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', 
    #     widget=forms.RadioSelect(attrs={}))
    # reading_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', 
    #     widget=forms.RadioSelect(attrs={}))
    # writing_skill = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', 
    #     widget=forms.RadioSelect(attrs={}))




    computer_skill1 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill2 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    computer_skill3 = forms.CharField(required=False,max_length=200, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
  
    level_computer_skill1 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill2 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
    level_computer_skill3 = forms.ChoiceField(choices = SKILL_CHOICES, label="",initial='', widget=forms.Select(attrs={'class': 'uk-select'}))
        
    # disability_cate1 = forms.ChoiceField(choices = DIS_CATE_CHOICES, label="",initial='', 
    #     widget=forms.Select(attrs={'class': 'uk-select','id':'disability_cate'}))
    # disability_cate2 = forms.ChoiceField(choices = DIS_CATE_CHOICES, label="",initial='', 
    #     widget=forms.Select(attrs={'class': 'uk-select','id':'disability_cate'}))
    # disability_cate3 = forms.ChoiceField(choices = DIS_CATE_CHOICES, label="",initial='', 
    #     widget=forms.Select(attrs={'class': 'uk-select','id':'disability_cate'}))

    # disability_level = forms.ChoiceField(choices = DIS_LEVEL_CHOICES, label="",initial='', 
    #     widget=forms.Select(attrs={'class': 'uk-select'}))
    working_time = forms.ChoiceField(choices = WORKING_TIME_CHOICES, label="",initial='', 
        widget=forms.Select(attrs={'class': 'uk-select'}))
    # working_time_range1 = forms.DateField(widget=AdminDateWidget())
    #  = start_datetime=forms.SplitDateTimeField(input_time_formats=['%I:%M %p'])
    # working_time_range2 = forms.SplitDateTimeFieldld(widget=SelectTimeWidget(minute_step=10, second_step=10))
    work_from_hour =forms.TimeField(initial=' ',widget=forms.TimeInput(format='%H:%M %p',attrs={'class': 'uk-input','id':'timepicker1'}))

    work_to_hour =forms.TimeField(initial='.',widget=forms.TimeInput(format='%H:%M %p',attrs={'class': 'uk-input','id':'timepicker2'}))
    work_type =forms.CharField(max_length=300, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
    disabled_welfare = forms.CharField(required=False,max_length=500, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    
    history_of_education  = forms.ChoiceField(choices = GRADUATE_CHOICES,  label="",initial='',
        widget=forms.Select(attrs={'class': 'uk-select'}))
 
    disability_cate = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DIS_CATE_CHOICES,)
    
    # qualification =  forms.CharField(max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification2 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification3 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification4 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification5 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification6 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification7 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification8 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification9 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    # qualification10 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	





