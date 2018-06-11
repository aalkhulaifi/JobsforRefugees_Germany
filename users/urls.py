from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_path, name='registration'),
    path('tasker/signup/', views.tasker_signup, name='taskersignup'),
    path('signup/', views.user_signup, name='signup'),
    path('signin/', views.user_signin, name='signin'),
    path('signout/', views.user_logout, name='signout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.user_edit_profile, name='edit_profile'),
    path('tasker_edit_profile/', views.tasker_edit_profile, name='tasker_edit_profile'),
    path('sent_task/<int:pk>/', views.sent_task, name= 'request'),
    path('request_list/', views.request_list, name = 'request_list' ),
    path('task_list/', views.task_list, name = 'task_list' ),
    path('tasker_notification/', views.tasker_notification, name = 'tasker_notification' ),
    path('tasker_notifications/<int:pk>/', views.tasker_notifications, name = 'tasker_notifications' ),
    path('user_notification/', views.user_notification, name = 'user_notification' ),
    path('user_notifications/<int:pk>/', views.user_notifications, name = 'user_notifications' ),
    path('create/', views.create_request, name = 'create_request' ),
    path('accept/<int:request_id>/', views.accepted_request, name = 'accept' ),
    path('deni/<int:request_id>/', views.deni_request, name = 'deni' ),

]
