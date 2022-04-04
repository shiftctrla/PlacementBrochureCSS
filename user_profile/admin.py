from django.contrib import admin
from .models import (
    Profile,
    Experience,
    Education,
)


admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
