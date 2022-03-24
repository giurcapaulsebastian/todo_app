from todolist.models import TodoItem
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help="Deletes list items that are completed"

    def handle(self, *args, **options):
        TodoItem.objects.filter(is_completed=True).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted completed items '))