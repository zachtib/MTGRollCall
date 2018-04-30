from datetime import date
from django.core.management.base import BaseCommand, CommandError

from event.models import Event


class Command(BaseCommand):
    help = 'Clean up past events'

    def handle(self, *args, **kwargs):
        result = Event.objects.filter(date__lt=date.today()).delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {result[0]} event(s)'))
