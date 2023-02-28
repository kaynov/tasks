from rest_framework.routers import DefaultRouter
from .views import TasksViewSet

router = DefaultRouter()

app_name = "taskslistapp"

router.register(
    prefix="tasks",
    viewset=TasksViewSet,
    basename="tasks",
)

urlpatterns = router.urls
