from django.db import models
from authentication.models import User

class Follower(models.Model):
    myfollow = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='myfollow')
    def __str__(self):
        return str(self.id)


class Following(models.Model):
    myfollowing = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='myfollowing')
    def __str__(self):
        return str(self.id)


