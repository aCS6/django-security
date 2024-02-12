from django.urls import path
# for password management
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user-logout', views.user_logout, name='user-logout'),
    
    # password management urls
    
    # Submit user email form
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'), name='reset_password'),
    
    # Success template for -> Email sent for reset password
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_sent.html'), name='password_reset_done'),
    
    # Send a link to the user email -> user can reset password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset_confirm'),
    
    # Password has change url
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'), name='password_reset_complete'),
    
    # Account locked
    path('account-locked', views.account_locked, name='account-locked'),
]