from django.urls import path

from . import views

app_name = 'portfolios'
urlpatterns = [
    path('', views.PortfoliosView.as_view(), name='portfolios'),
    path('<slug:slug>/', views.PortfolioView.as_view(), name='portfolio'),
]
