from django.db import models

class Student(models.Model):

    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]

    batch_year = models.IntegerField()
    graduation_year = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact_number = models.CharField(max_length=10)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    skills = models.TextField(max_length=500)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.name
