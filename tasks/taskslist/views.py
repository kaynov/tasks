from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

from .models import Tasks


class ListViewFull(ListView):
    context_object_name = "tasks_"
    queryset = Tasks.objects.all()
    template_name = "tasks_list.html"


class ListViewOnFull(ListView):
    context_object_name = "tasks_"
    queryset = Tasks.objects.filter(status=True)
    template_name = "tasks_list_on.html"


class ListViewOffFull(ListView):
    context_object_name = "tasks_"
    queryset = Tasks.objects.filter(status=False)
    template_name = "tasks_list_off.html"


class TasksCreateView(CreateView):
    model = Tasks
    fields = ["name", "status"]
    template_name = "tasks_create.html"
    success_url = reverse_lazy("load")


class TasksDeleteView(DeleteView):
    model = Tasks
    template_name = "tasks_delete.html"
    success_url = reverse_lazy("load")


class TasksUpdateView(UpdateView):
    model = Tasks
    fields = ["name", "status"]
    template_name = "tasks_edit.html"
    success_url = reverse_lazy("load")
