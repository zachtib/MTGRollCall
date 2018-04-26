import uuid

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from mtgrollcall import settings
from playgroup.models import PlayGroup, Membership


class Event(models.Model):
    playgroup = models.ForeignKey(PlayGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    date = models.DateField()

    def viewable_by(self, user: User):
        if self.playgroup.owner == user:
            return True
        return False

    def __str__(self):
        return self.name


class Invitation(models.Model):
    NOT_RESPONDED = 'NR'
    RESPONSE_YES = 'YE'
    RESPONSE_NO = 'NO'

    RESPONSE_CHOICES = (
        (NOT_RESPONDED, 'Not responded'),
        (RESPONSE_YES, 'Yes'),
        (RESPONSE_NO, 'No'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='invitations', on_delete=models.CASCADE)
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    response = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=NOT_RESPONDED
    )

    @staticmethod
    def get_choice_display_name(code):
        for item in Invitation.RESPONSE_CHOICES:
            if item[0] == code:
                return item[1]
        return 'None'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('event:invitation', kwargs={
            'event_id': self.event_id,
            'invite_id': self.id,
        })
        

    def send_email(self):
        subject = "You've been invited"
        message = render_to_string('email/invite.html', {
            'invitation': self,
        })

        send_mail(subject,
                  '',
                  f'noreply@{ settings.MAILGUN_DOMAIN }',
                  (self.member.email, ),
                  html_message=message)
