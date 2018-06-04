from django.urls import path
from .views import UserCreateAPIView,UserLoginAPIView ,TaskerCreateAPIView,TaskerLoginAPIView,Task_RequestAPIView,Task_RequesListView, Task_RequesDetailView

urlpatterns = [
	path('signup/', UserCreateAPIView.as_view(), name='signup'),
	path('signin/', UserLoginAPIView.as_view(), name='signin'),
	path('taskersignin/', TaskerLoginAPIView.as_view(), name='taskersignin'),
	path('taskersignup/', TaskerCreateAPIView.as_view(), name='taskersignup'),
	path('task/', Task_RequestAPIView.as_view(), name='task'),
	path('list/', Task_RequesListView.as_view(), name='list'),
	path('detail/<int:object_id>/', Task_RequesDetailView.as_view(), name='detail'),

]