from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField,Select
from datetime import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
	
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	profile_picture=models.ImageField(upload_to="profilePicture/",default="")
	created_at = models.DateTimeField(blank=True,null=True,)
	def __str__(self):
		return "%s"%(self.user)

class DisabilityInfo(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True,null=True)
	first_name = models.CharField(max_length=100,editable=True )
	last_name = models.CharField(max_length=100,editable=True )
	disable_id = models.CharField(max_length=10,blank=True,null=True,)
	citizen_id = models.CharField(max_length=10,blank=True,null=True,)
	region = models.CharField(max_length=10,blank=True,null=True,)
	birth_date = models.DateTimeField(auto_now_add=True,null=True,)
	age = models.IntegerField()
	sex = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
	registration_address = models.CharField(max_length=5000,blank=True,null=True,default="ไม่ระบุ")
	registration_province = models.CharField(max_length=5000,blank=True,null=True,default="ไม่ระบุ")
	current_address = models.CharField(max_length=5000,blank=True,null=True,default="ไม่ระบุ")
	current_province = models.CharField(max_length=5000,blank=True,null=True,default="ไม่ระบุ")
	graduate = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	graduate_year = models.CharField(max_length=10,blank=True,null=True,default="ไม่ระบุ")
	educational_institution = models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	faculty = models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	branch = models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	

	honor_name =  models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	honor_year =  models.CharField(max_length=10,blank=True,null=True,default="ไม่ระบุ")
	agency_honor = models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	hobbies = models.CharField(max_length=2500,blank=True,null=True,default="ไม่ระบุ")
	interesting_work_cate = models.CharField(max_length=2500,blank=True,null=True,default="ไม่ระบุ")

	language1 = models.CharField(max_length=250,blank=True,null=True,default="ไม่ระบุ")
	listen_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	speaking_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	reading_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	writing_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	language2 = models.CharField(max_length=250,blank=True,null=True,default="ไม่ระบุ")
	listen_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	speaking_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	reading_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	writing_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	language3 = models.CharField(max_length=250,blank=True,null=True,default="ไม่ระบุ")
	listen_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	speaking_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	reading_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	writing_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	language4 = models.CharField(max_length=250,blank=True,null=True,default="ไม่ระบุ")
	listen_skill4 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	speaking_skill4 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	reading_skill4 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	writing_skill4 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")

	computer_skill1 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill2 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill3 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill4 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill5 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")

	level_computer_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill4 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill5 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	congenital_disease = models.CharField(max_length=500,blank=True,null=True,default="ไม่ระบุ")
	lawsuit = models.CharField(max_length=10,blank=True,null=True,default="ไม่ระบุ")
	


	helping_myself = models.BooleanField(default=False)
	traveling_by_myself = models.BooleanField(default=False)
	work_in_other_province = models.BooleanField(default=False)
	working_time = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	current_status = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")

	disability_cate = models.CharField(max_length=100)
	disability_level = models.CharField(max_length=10,blank=True,null=True,default="1")
	disability_reason = models.CharField(max_length=50,blank=True,null=True,default="1")
	disabled_year = models.CharField(max_length=10,blank=True,null=True,default="")
	disabled_equiptment = models.CharField(max_length=50,blank=True,null=True,default="")



	job_exp = models.CharField(max_length=10,default="",blank=True,null=True,)
	last_company_name = models.CharField(max_length=1000,blank=True,null=True,)
	last_company_province = models.CharField(max_length=100,blank=True,null=True,)
	position = models.CharField(max_length=300,blank=True,null=True,)
	working_start_date = models.DateTimeField(auto_now_add=True,null=True,)
	working_end_date = models.DateTimeField(auto_now_add=True,null=True,)
	quit_job_reason = models.CharField(max_length=500,blank=True,null=True,)


	job_interest1 = models.CharField(max_length=100,blank=True,null=True,)
	job_interest2 = models.CharField(max_length=100,blank=True,null=True,)
	job_interest3 = models.CharField(max_length=100,blank=True,null=True,)


	expected_salary1 = models.CharField(max_length=100,blank=True,null=True,)
	expected_salary2 = models.CharField(max_length=100,blank=True,null=True,)
	expected_salary3 = models.CharField(max_length=100,blank=True,null=True,)
	expected_welfare = models.CharField(max_length=1000)


	created_at = models.DateTimeField(auto_now_add=True,null=True,)	

	def __str__(self):
		return "%s"%(self.first_name)


		
class CompanyInfo(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True,null=True)
	th_name = models.CharField(max_length=100,editable=True )
	en_name = models.CharField(max_length=100,editable=True )
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
	hr_no = models.CharField(max_length=100,editable=True,blank=True,null=True )
	address = models.CharField(max_length=5000,default="ไม่ระบุ")
	info = models.CharField(max_length=5000,default="ไม่ระบุ")
	website = models.CharField(max_length=50,default="ไม่ระบุ")
	fax = models.CharField(max_length=30)
	company_type = models.CharField(max_length=100)
	get_more_info = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	
	def __str__(self):
		return "%s"%(self.th_name)


class Job(models.Model): 
	company = models.ForeignKey(CompanyInfo, on_delete=models.SET_NULL,blank=True,null=True)
	title_th = models.CharField(max_length=100,editable=True )
	title_en = models.CharField(max_length=100,editable=True )
	email = models.EmailField(max_length=100,blank=True,null=True)
	age1 = models.IntegerField(blank=True,null=True)
	age2 = models.IntegerField(blank=True,null=True)
	sex = models.CharField(max_length=10)
	# detail = RichTextField(blank=True,null=True)
	detail = models.CharField(max_length=5000,default="ไม่ระบุ",blank=True,null=True)
	language = models.CharField(max_length=1000,blank=True,null=True,default="ไม่ระบุ")
	# listen_skill = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	# speaking_skill = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	# reading_skill = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	# writing_skill = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")

	computer_skill1 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill2 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	computer_skill3 = models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")

	level_computer_skill1 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill2 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	level_computer_skill3 = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")


	working_time = models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	work_from_hour =models.TimeField(null=True, blank=True)
	work_to_hour =models.TimeField(null=True, blank=True)
	work_type =models.CharField(max_length=250,blank=True,null=True,default="ไม่ระบุ")

	disability_cate = models.CharField(max_length=100)
	history_of_education =models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	disabled_welfare =models.CharField(max_length=100,blank=True,null=True,default="ไม่ระบุ")
	# disability_level = models.CharField(max_length=10,blank=True,null=True,default="1")
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
	salary =models.CharField(max_length=50,blank=True,null=True,default="ไม่ระบุ")
	 # = models.IntegerField(blank=True,null=True)
	# salary2 = models.IntegerField(blank=True,null=True)
	# qualification = models.CharField(max_length=5000,blank=True,null=True)
	province = models.CharField(max_length=150,default="",blank=True,null=True,)
	address = models.CharField(max_length=5000,default="ไม่ระบุ")
	# province = models.CharField(max_length=150,default="",blank=True,null=True,)



	created_at = models.DateTimeField(auto_now_add=True,null=True,)	
	def __str__(self):
		return "%s"%(self.title_th)


class Contact(models.Model):
	email= models.CharField(max_length=100,editable=True )
	name = models.CharField(max_length=100,editable=True )
	phone= models.CharField(max_length=20,editable=True )
	subject = models.CharField(max_length=100,editable=True )
	message= models.CharField(max_length=1000,editable=True )

class Notifications(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	job = models.ForeignKey(Job,on_delete=models.SET_NULL,blank=True,null=True)
	tarket = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
	action = models.CharField(max_length=20,editable=True )
	obj = models.CharField(max_length=200,editable=True ,blank=True,null=True)
	is_read = models.BooleanField(default=False)
	message= models.CharField(max_length=5000,editable=True,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	

class InviteProcess(models.Model):
	STATUS_CHOICES = (
		('ยังไม่ส่งคำเชิญ', 'ยังไม่ส่งคำเชิญ'),
		('ส่งคำเชิญ', 'ส่งคำเชิญ'),
		('ตอบรับคำเชิญ', 'ตอบรับคำเชิญ'),
		('สมัครงาน', 'สมัครงาน'),
		('ปฏิเสธงาน', 'ปฏิเสธงาน'),
	
	)

	disability = models.ForeignKey(DisabilityInfo, on_delete=models.SET_NULL,blank=True,null=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	job = models.ForeignKey(Job, on_delete=models.SET_NULL,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	

class Save(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	target = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
	name = models.CharField(max_length=1000,editable=True,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
