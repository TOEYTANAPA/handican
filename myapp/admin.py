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

class ContactAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Contact._meta.fields]
admin.site.register(Contact, ContactAdmin)


class JobAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Job._meta.fields]
admin.site.register(Job, JobAdmin)

class NotificationsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Notifications._meta.fields]
admin.site.register(Notifications, NotificationsAdmin)

class SaveAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Save._meta.fields]
admin.site.register(Save, SaveAdmin)


class InviteProcessAdmin(admin.ModelAdmin):
	list_display=[f.name for f in InviteProcess._meta.fields]
admin.site.register(InviteProcess, InviteProcessAdmin)