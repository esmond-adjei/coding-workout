from django.urls import path
from .views import TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate, RegisterUser, TaskLogin, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
	# path('', home, name='home'),
	path('', TaskLogin.as_view(), name = 'login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
	path('register/', RegisterUser.as_view(), name='register'),
	
	path('task/', TaskList.as_view(), name='tasks'),
	path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
	path('task-create/', TaskCreate.as_view(), name='task-create'),
	path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
	path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]