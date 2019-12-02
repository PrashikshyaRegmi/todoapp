from django.views.generic import *
from .form import *
from django.urls import reverse_lazy


class CreateTaskView(CreateView):
    template_name = 'taskcreate.html'
    form_class = ItemForm
    success_url = "/"

class ListTaskView(ListView):
    template_name = 'tasklist.html'
    model = Item
    context_object_name = 'alltasks'

class UpdateTaskView(UpdateView):
    template_name = 'taskcreate.html'
    model= Item
    form_class = ItemForm
    success_url = '/'

class DeleteTaskView(DeleteView):
    template_name = 'taskdelete.html'
    model = Item
    success_url ='/'
