from django.urls import path

from . import views

app_name = 'stores'
urlpatterns = [
    path('', views.StoresView.as_view(), name='stores'),
    path('<slug:slug>/', views.StoreView.as_view(), name='store'),
]
