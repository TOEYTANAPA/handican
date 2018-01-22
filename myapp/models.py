from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField,Select
from datetime import datetime
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
	phone_no = models.CharField(max_length=20,default="-")
	address = models.CharField(max_length=1000,blank=True,null=True,default="-")
	disability_cate = models.CharField(max_length=100)
	lastest_job = models.CharField(max_length=100)
	lastest_office = models.CharField(max_length=100)
	expected_salary = models.CharField(max_length=50)
	expected_welfare = models.CharField(max_length=500)
	talent = models.CharField(max_length=300)
	talent2 = models.CharField(max_length=300)
	talent3 = models.CharField(max_length=300)
	more_resume = models.FileField(upload_to="resume/",default="")
	get_more_info = models.BooleanField()
		
class CompanyInfo(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,blank=True,null=True)
	th_name = models.CharField(max_length=100,editable=True )
	en_name = models.CharField(max_length=100,editable=True )
	phone_no = models.CharField(max_length=20,default="-")
	address = models.CharField(max_length=1000,default="-")
	info = models.CharField(max_length=1000,default="-")
	website = models.CharField(max_length=50)
	fax = models.CharField(max_length=30)
	company_type = models.CharField(max_length=100)
	get_more_info = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	


class Job(models.Model): 
	company = models.ForeignKey(CompanyInfo, on_delete=models.SET_NULL,blank=True,null=True)
	title_th = models.CharField(max_length=100,editable=True )
	title_en = models.CharField(max_length=100,editable=True )
	age = models.IntegerField(blank=True,null=True)
	sex = models.CharField(max_length=10)
	detail = models.CharField(max_length=2000,default="")
	disability_cate = models.CharField(max_length=100)
	traveling = models.CharField(max_length=1000)
	welfare = models.CharField(max_length=1000)
	salary = models.CharField(max_length=50)
	company_image=models.ImageField(upload_to="createJob/",default="")
	created_at = models.DateTimeField(auto_now_add=True,null=True,)	


class Contact(models.Model):
	email= models.CharField(max_length=100,editable=True )
	name = models.CharField(max_length=100,editable=True )
	phone= models.CharField(max_length=20,editable=True )
	subject = models.CharField(max_length=100,editable=True )
	message= models.CharField(max_length=1000,editable=True )

class Notifications(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	tarket = models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
	action = models.CharField(max_length=20,editable=True )
	is_read = models.BooleanField(default=False)
