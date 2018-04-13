from django.contrib.auth.models import User
from django.db import models


class PlayGroup(models.Model):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(User)