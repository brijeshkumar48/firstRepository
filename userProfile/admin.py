from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Peron)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','gender','dob','mobile_number','email','address','objective','others','qrCode']

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['org_name','person','location','current_designation','salary','projects','work_description']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['course_name','short_name','university_name','description']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['laungue_name','institute_name','cert_description']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name','perce_of_proficiency']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']