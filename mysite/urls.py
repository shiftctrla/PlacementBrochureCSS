from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home_view, name='home'),
    path('profiles/<int:pk>/', core_views.profile_detail_view, name='profile-detail'),

    path('register/', account_views.registration_view, name='register'),
    path('logout/', account_views.logout_view, name="logout"),
    path('login/', account_views.login_view, name="login")



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# CUK Placement Brochure Admin Site Customizations
admin.site.site_header = "SOET Placement Brochure ADMIN"
admin.site.site_title = "SOET Admin"
admin.site.index_title = "Welcome to Placement Brochure Admin Panel"
