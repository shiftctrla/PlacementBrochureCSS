from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# CUK Placement Brochure Admin Site Customizations
admin.site.site_header = "SOET Placement Brochure ADMIN"
admin.site.site_title = "SOET Admin"
admin.site.index_title = "Welcome to Placement Brochure Admin Panel"
