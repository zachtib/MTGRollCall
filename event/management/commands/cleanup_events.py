from datetime import date
from django.core.management.base import BaseCommand, CommandError

from event.models import Event


class Command(BaseCommand):
    help = 'Clean up past events'

    def handle(self, *args, **kwargs):
        count = 0
        for event in Event.objects.filter(date__lt=date.today()):
            event.delete()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} event(s)'))
