from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

auth_patterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('confirm-email/', views.ConfirmEmailView.as_view(), name='confirm_email'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('confirm-token/', views.ConfirmTokenView.as_view(), name='confirm_token'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete/', views.DeleteAccountView.as_view(), name='delete'),
]

profile_patterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change-profile/', views.ChangeProfileView.as_view(), name='change_profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]

app_name = 'accounts'
urlpatterns = [
    path('', include(auth_patterns)),
    path('', include(profile_patterns)),
]
