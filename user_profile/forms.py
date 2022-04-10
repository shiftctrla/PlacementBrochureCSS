from django import forms
from .models import Profile





class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'profile_pic',
            'date_of_birth',
            'contact_number',
            'address',
            'gender',
            'resume'
        ]
