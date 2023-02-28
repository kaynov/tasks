from django_filters import rest_framework as dj_filters
from .models import Tasks


class TasksFilterSet(dj_filters.FilterSet):
    title = dj_filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_active = dj_filters.CharFilter(field_name="status", lookup_expr="exact",
                                      exclude=True)

    order_by_field = "ordering"

    class Meta:
        model = Tasks
        fields = [
            "name",
            "status",
        ]
