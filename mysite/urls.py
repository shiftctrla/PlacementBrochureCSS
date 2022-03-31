from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core import views as core_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home_view, name='home'),
    path('profiles/<int:pk>/', core_views.profile_detail_view, name='profile-detail'),

    path('register/', account_views.registration_view, name='register'),
    path('logout/', account_views.logout_view, name="logout"),
    path('login/', account_views.login_view, name="login"),





    # PASSWORD RESET VIEWS

    path('password-reset/',
        auth_views.PasswordResetView.as_view(
                template_name='account/password_reset.html'
            ),
        name='password_reset'),


    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
                template_name='account/password_reset_done.html'
            ),
        name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(
                template_name='account/password_reset_confirm.html'
            ),
        name='password_reset_confirm'),


    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
                template_name='account/password_reset_complete.html'
            ),
        name='password_reset_complete'),







]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# CUK Placement Brochure Admin Site
admin.site.site_header = "SOET Placement Brochure ADMIN"
admin.site.site_title = "SOET Admin"
admin.site.index_title = "Welcome to Placement Brochure Admin Panel"
