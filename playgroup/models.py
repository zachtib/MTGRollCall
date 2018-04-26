from django.contrib.auth.models import User
from django.db import models


class PlayGroup(models.Model):
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('playgroup:details', kwargs={
            'group_id': self.id,
        })

    def viewable_by(self, user: User):
        if self.owner == user:
            return True
        return False

    def __str__(self):
        return self.name


class Membership(models.Model):
    playgroup = models.ForeignKey(PlayGroup, related_name='members',
                                  on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    email = models.EmailField()

    @property
    def is_registered(self):
        # TODO: Implement when user registrations are available
        return False

    def __str__(self):
        return self.display_name
