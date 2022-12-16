from django.db import models

# Create your models here.


class Peron(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    dob = models.CharField(max_length=30, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    objective = models.TextField()
    others = models.CharField(max_length=200, null=True, blank=True)
    pdf = models.FileField(upload_to='resume',null=True, blank=True)
    qrCode = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    person = models.ForeignKey(Peron, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    completion_date = models.CharField(max_length=100, null=True, blank=True)
    percentage = models.CharField(max_length=100, null=True, blank=True)


class Certification(models.Model):
    person = models.ForeignKey(Peron, on_delete=models.CASCADE)
    laungue_name = models.CharField(max_length=100, null=True, blank=True)
    institute_name = models.CharField(max_length=100, null=True, blank=True)
    cert_description = models.CharField(max_length=100, null=True, blank=True)


class Skill(models.Model):
    person = models.ForeignKey(Peron, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    perce_of_proficiency = models.CharField(max_length=100, null=True, blank=True)


class Organization(models.Model):
    person = models.ForeignKey(Peron, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    current_designation = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    projects = models.CharField(max_length=100, null=True, blank=True)
    work_description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.org_name

class ContactUs(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    message = models.TextField(null=True, blank=True)