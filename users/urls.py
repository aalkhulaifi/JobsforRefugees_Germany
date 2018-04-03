from django.urls import path
from . import views
app_name='users'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_logout, name='signout'),
]