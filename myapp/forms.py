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
    (1, 'หญิง'),
    (3, 'หญิง, ชาย')
    )

	title_th =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	title_en =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	job_detail =  forms.CharField(max_length=2000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
	disability_type =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
	age1 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	age2 =  forms.IntegerField(required=False,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))

	sex = forms.ChoiceField(required=False,choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
	# salary = forms.ChoiceField(choices=(('น้อยกว่า 10,000','น้อยกว่า 10,000' ),('10,000-19,000','10,000-19,000')
 #        ,('20,000-29,999','20,000-29,999'),('30,000-39,000','30,000-39,000'),('40,000-49,000','40,000-49,000')
 #        ,('50,000 ขึ้นไป','50,000 ขึ้นไป')), required=True, widget=forms.Select())

	salary1 =  forms.IntegerField(help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	salary2 =  forms.IntegerField(help_text='',widget=forms.TextInput(attrs={'class': 'uk-input','type':'number'}))
	welfare = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
	traveling = forms.CharField(max_length=1000, help_text='',widget=forms.Textarea(attrs={'rows': 3,'class': 'uk-textarea', }))
	qualification = forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
	company_image = forms.FileField()
