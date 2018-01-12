from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Profile._meta.fields]
admin.site.register(Profile, ProfileAdmin)

class DisabilityInfoAdmin(admin.ModelAdmin):
	list_display=[f.name for f in DisabilityInfo._meta.fields]
admin.site.register(DisabilityInfo, DisabilityInfoAdmin)

class CompanyInfoAdmin(admin.ModelAdmin):
	list_display=[f.name for f in CompanyInfo._meta.fields]
admin.site.register(CompanyInfo, CompanyInfoAdmin)