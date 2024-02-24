from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('signup/', views.signup, name='signup'),   
    path('edit/', views.profile_edit, name='profile_edit'),
    path('password_change/', views.password_change, name='password_change'),
]
