from django.urls import path
from .views import home, signup, profile, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("profile/", profile, name="profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    
    # Django authentication views
    path("login/", auth_views.LoginView.as_view(template_name="login.html", next_page="/profile"), name="login"),
    path("signup/", signup, name="signup"),
    
    # Password reset views
    path("forgot-password/", auth_views.PasswordResetView.as_view(template_name="forget_password.html"), name="password_reset"),
    path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    
    path("password-change/", auth_views.PasswordChangeView.as_view(template_name="password_change.html"), name="password_change"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
]
