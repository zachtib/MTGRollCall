from django.contrib.auth.models import User
from django.db import models


class PlayGroup(models.Model):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def viewable_by(self, user: User):
        if self.owner == user:
            return True
        return False

    def __str__(self):
        return self.name


class Membership(models.Model):
    playgroup = models.ForeignKey(PlayGroup, related_name='membership',
                                  on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.email} is in {self.playgroup}'
