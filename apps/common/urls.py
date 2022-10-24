from django.urls import path

from . import views

app_name = 'common'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact_us'),
    path('privacy/', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('cookies/', views.CookiesView.as_view(), name='cookies'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('impressum/', views.ImpressumView.as_view(), name='impressum'),
    path('switch-language/', views.SwitchLanguageView.as_view(), name='switch_language'),
    path('subscribe/', views.SubscribeView.as_view(), name='subscribe'),
]
