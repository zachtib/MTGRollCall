from django.core.management.base import BaseCommand, CommandError
from event.models import Invitation


class Command(BaseCommand):
    help = 'Send unsent invitations'

    def handle(self, *args, **kwargs):
        count = 0
        for invite in Invitation.objects.filter(sent=False):
            invite.send_email()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Sent {count} invitation(s)'))
