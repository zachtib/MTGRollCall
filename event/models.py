import uuid

from django.contrib.auth.models import User
from django.db import models

from playgroup.models import PlayGroup, Membership


class Event(models.Model):
    playgroup = models.ForeignKey(PlayGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    date = models.DateField()

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