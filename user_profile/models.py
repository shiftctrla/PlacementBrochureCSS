from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Experience(models.Model):
    designation = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    start_from = models.DateField()
    end_at = models.DateField()


    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.designation


class Education(models.Model):
    degree = models.CharField(max_length=255)
    year_of_passing = models.DateField()
    organisation = models.CharField(max_length=255)
    score = models.FloatField()
    remarks = models.TextField()

    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.degree


class Project(models.Model):
    title = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)

    github_repo = models.CharField(max_length=1024, null=True)


    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title




class Profile(models.Model):

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, default="Student")
    last_name = models.CharField(max_length=60, null=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    resume = models.FileField(upload_to='resumes', null=True)


    def __str__(self):
        return f'{self.user.username} Profile'
