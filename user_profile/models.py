from django.db import models
from django.conf import settings


class Experience(models.Model):
    designation = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    start_from = models.DateField()
    end_at = models.DateField()

    
    profile = models.ForeignKey(Profile, on_delete=models.CASCASE)


class Education(models.Model):
    degree = models.CharField(max_length=255)
    year_of_passing = models.DateField()
    organisation = models.CharField(max_length=255)
    score = models.FloatField()
    remarks = models.TextField()

    profile = models.ForeignKey(Profile, on_delete=models.CASCASE)

class Profile(models.Model):

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    resume = models.FileField()
