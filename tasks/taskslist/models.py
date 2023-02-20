from django.db import models

from datetime import datetime


class Tasks(models.Model):

    name = models.CharField(
        max_length=100, help_text="Список задач"
    )
    status = models.BooleanField(
        default=False, help_text="Статус задачи"
    )
    start = models.DateTimeField(
        auto_now_add=True, help_text="Время начала задания"
    )
    end = models.DateTimeField(
        blank=True, null=True, help_text="Время выполнения задания"
    )

    class Meta:
        verbose_name_plural = "Задачи"

    def save(self, *args, **kwargs) -> None:
        if self.status and not self.end:
            self.end = datetime.now()
        elif not self.status and self.end:
            self.timestamp_end = None
        return super().save(*args, **kwargs)

