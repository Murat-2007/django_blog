from django.urls import path 
from .views import register, user_login, user_logout, user_profile, user_settings, user_about, user_password_change

urlpatterns = [
    path('register/', view=register, name='register'),
    path('login/', view=user_login, name='user_login'),
    path('logout/', view=user_logout, name='user_logout'),
    path('settings/', view=user_settings, name='user_settings'),
    path('password_change/', view=user_password_change, name='password_change'),
    path('<username>/', view=user_profile, name='user_profile'),
    path('<username>/about', view=user_about, name='user_about'),
]