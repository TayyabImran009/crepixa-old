from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('<slug:slug>/', views.PostView.as_view(), name='post'),
]
