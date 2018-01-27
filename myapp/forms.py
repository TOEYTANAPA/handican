from django import forms
# from django.contrib.auth.models import User
# from myapp.models import Profile
from froala_editor.widgets import FroalaEditor

from ckeditor.fields import RichTextFormField


class ContactForm(forms.Form):
    name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    email =  forms.EmailField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    phone =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    subject =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    message =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
   



class CreateJobForm(forms.Form):
	GENDER_CHOICES = (
    (0, 'ชาย'),
    (1, 'หญิง'),
    (2, 'หญิง, ชาย')
    )

	title_th =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	title_en =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	# job_detail =  forms.CharField(max_length=2000, help_text='',widget=forms.Textarea(attrs={'id':'jobde','rows': 5,'class': 'uk-textarea', }))
	disability_type =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	age1 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	age2 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	email =  forms.EmailField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	sex = forms.ChoiceField(required=False,choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
	phone_no =  forms.CharField(max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	job_detail = RichTextFormField()
	# welfare =  RichTextFormField()
	salary1 =  forms.IntegerField(help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	salary2 =  forms.IntegerField(help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	# welfare = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
	qualification =  forms.CharField(max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification2 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification3 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification4 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification5 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification6 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification7 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification8 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification9 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	qualification10 =  forms.CharField(required=False,max_length=2000,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	location = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
	province =  forms.CharField(max_length=250, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
