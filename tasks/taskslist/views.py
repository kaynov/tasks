from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from .models import Tasks
from rest_framework import viewsets, mixins
from rest_framework.schemas.openapi import AutoSchema
from .serializers import TasksSerializer
from .filters import TasksFilterSet


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


class TasksViewSet(
    mixins.ListModelMixin,  # GET /tasks
    mixins.CreateModelMixin,  # POST /tasks
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet
):
    queryset = Tasks.objects.all().order_by("-id")
    serializer_class = TasksSerializer
    filterset_class = TasksFilterSet

    schema = AutoSchema(
        tags=['TasksList'],
        component_name='Tasks',
        operation_id_base='Tasks',
    )
