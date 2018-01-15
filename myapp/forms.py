from django import forms
# from django.contrib.auth.models import User
# from myapp.models import Profile



class ContactForm(forms.Form):
    name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    email =  forms.EmailField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    phone =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    subject =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    message =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
   



class CreateJobForm(forms.Form):
	GENDER_CHOICES = (
    (0, 'ชาย'),
    (1, 'หญิง')
    )

	title_th =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	title_en =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	job_detail =  forms.CharField(max_length=2000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
	disability_type =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	age =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	sex = forms.ChoiceField(required=False,choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
	salary = forms.CharField(max_length=50, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	welfare = forms.CharField(max_length=1000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
	traveling = forms.CharField(max_length=1000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
	company_image = forms.FileField()
