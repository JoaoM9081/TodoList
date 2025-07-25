from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

# Create your views here.
class TaskList(ListView):
    model = Todo
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Todo.objects.all()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

class TaskDetail(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todoList/task.html'

class TaskCreate(CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    template_name = 'todoList/task_form.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    template_name = 'todoList/task_form.html'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Todo
    context_object_name = 'task'
    template_name = 'todoList/delete.html'
    success_url = reverse_lazy('tasks')