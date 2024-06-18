# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # URL pattern for registration
    path('login/', views.user_login, name='login'),  # URL pattern for login
    path('logout/', views.user_logout, name='logout'),  # URL pattern for logout
    # Other URL patterns for your application
]
