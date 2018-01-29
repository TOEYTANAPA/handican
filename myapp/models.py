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
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	def __str__(self):
		return "%s"%(self.user)

class DisabilityInfo(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True,null=True)
	first_name = models.CharField(max_length=100,editable=True )
	last_name = models.CharField(max_length=100,editable=True )
	age = models.IntegerField()
	sex = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
	address = models.CharField(max_length=5000,blank=True,null=True,default="ไม่ระบุ")
	disability_cate = models.CharField(max_length=100)
	job_interest = models.CharField(max_length=100)
	job_exp = models.CharField(max_length=5000,default="")
	expected_salary1 = models.IntegerField(blank=True,null=True,)
	expected_salary2 = models.IntegerField(blank=True,null=True,)
	expected_welfare = models.CharField(max_length=1000)
	talent = models.CharField(max_length=1000)
	talent2 = models.CharField(max_length=1000,default="")
	talent3 = models.CharField(max_length=1000,default="")
	province = models.CharField(max_length=250,default="",blank=True,null=True,)
	more_resume = models.FileField(upload_to="resume/",default=None,blank=True,null=True,)
	get_more_info = models.BooleanField()
	def __str__(self):
		return "%s"%(self.first_name)
		
class CompanyInfo(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True,null=True)
	th_name = models.CharField(max_length=100,editable=True )
	en_name = models.CharField(max_length=100,editable=True )
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
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
	detail = RichTextField(blank=True,null=True)
	phone_no = models.CharField(max_length=20,default="ไม่ระบุ")
	disability_cate = models.CharField(max_length=100)
	salary1 = models.IntegerField(blank=True,null=True)
	salary2 = models.IntegerField(blank=True,null=True)
	qualification = models.CharField(max_length=5000,blank=True,null=True)
	province = models.CharField(max_length=250,default="",blank=True,null=True,)
	address = models.CharField(max_length=5000,default="ไม่ระบุ")


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
	
	)

	disability = models.ForeignKey(DisabilityInfo, on_delete=models.SET_NULL,blank=True,null=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	job = models.ForeignKey(Job, on_delete=models.SET_NULL,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	

class Save(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	target = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
