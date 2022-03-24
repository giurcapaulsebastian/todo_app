from asyncio.windows_events import NULL
from statistics import mode
from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'todolist_items'
