# myapp/management/commands/update_datetime.py
from django.core.management.base import BaseCommand
from django.utils import timezone
import pytz
from ...models import DataEntry

class Command(BaseCommand):
    help = 'Update naive datetimes to timezone-aware datetimes'

    def handle(self, *args, **kwargs):
        for entry in DataEntry.objects.all():
            if entry.added and entry.added.tzinfo is None:
                # Convert naive datetime to aware datetime
                entry.added = timezone.make_aware(entry.added, pytz.utc)
                entry.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated datetime fields'))
