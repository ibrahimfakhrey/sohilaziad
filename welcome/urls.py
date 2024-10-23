from django.urls import path
from .views import welcome_view,user_login,user_logout,register

urlpatterns = [
    path('', welcome_view, name='home'),
 path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),]
