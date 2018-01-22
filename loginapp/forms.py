from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    (0, 'ชาย'),
    (1, 'หญิง')
    )

    first_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    last_name =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    age =  forms.IntegerField( help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    sex = forms.ChoiceField(choices = GENDER_CHOICES, label="",initial='', widget=forms.Select())
    address =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    disability_cate =  forms.CharField(max_length=100, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    job_interest =  forms.CharField(required=False,max_length=2000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'})) 
    job_exp =  forms.CharField(max_length=5000, help_text='',widget=forms.Textarea(attrs={'rows': 5,'class': 'uk-textarea', }))
    expected_salary = forms.ChoiceField(choices=(('น้อยกว่า 10,000','น้อยกว่า 10,000' ),('10,000-19,000','10,000-19,000')
        ,('20,000-29,999','20,000-29,999'),('30,000-39,000','30,000-39,000'),('40,000-49,000','40,000-49,000')
        ,('50,000 ขึ้นไป','50,000 ขึ้นไป')), required=True, widget=forms.Select())

    phone_no =  forms.CharField(max_length=20,help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    expected_welfare =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    talent =  forms.CharField(max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    talent2 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    talent3 =  forms.CharField(required=False,max_length=1000, help_text='',widget=forms.TextInput(attrs={'class': 'uk-input'}))
    more_resume = forms.FileField(required=False,)
    profile_image = forms.FileField()
    get_more_info = forms.BooleanField(required=False,initial=False)

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
