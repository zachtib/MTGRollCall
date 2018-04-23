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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, related_name='invitations', on_delete=models.CASCADE)
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)