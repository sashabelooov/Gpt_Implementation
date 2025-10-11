from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login')
]