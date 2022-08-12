# from typing import List
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import Task


def home(request):
	return render(request, 'base/main.html')


class TaskLogin(LoginView):
	template_name = 'base/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('tasks')


class RegisterUser(FormView):
	template_name = 'base/register.html'
	form_class = UserCreationForm
	redirect_authenticator_user = True
	success_url = reverse_lazy('tasks')

	# def form_valid(self, form):
	# 	user = form.save()
	# 	if user is not None:
	# 		login(self.request, user)
	# 	return super(RegisterUser, self).form_valid(form)

	# def get(self, *args, **kwargs):
	# 	if self.request.user.is_authenticated:
	# 		return redirect('tasks')
	# 	return super(RegisterUser, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
	"uses view from 'ListView' and implement it in this class"
	model = Task
	context_object_name = 'tasks'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		context['count'] = context['tasks'].filter(complete=False).count()
		
		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['tasks'] = context['tasks'].filter(title__contains=search_input) # filter title by __icontaints, __startswith

		context['search_input'] = search_input
		return context


class TaskDetail(LoginRequiredMixin, DetailView):
	model = Task
	context_object_name = 'task'
	template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	fields = ['title', 'description','complete']
	template_name = 'base/task_create.html'
	success_url = reverse_lazy('tasks')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Task
	fields = ['title', 'description', 'complete']
	template_name = 'base/task_create.html'
	success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
	model = Task
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')