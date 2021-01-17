from django.db import models
from authentication.models import User
from Videos.models import Upload


class Like(models.Model):
    EXPRESSIONS = (
        ('1', 'love'),
        ('2', 'happy'),
        ('3', 'sad'),
        ('4', 'angry'),
    )
    likeuser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='likeuser')
    likevideo = models.ForeignKey(Upload, null=True, on_delete=models.SET_NULL, related_name='likevideo')
    like = models.BooleanField(null=True,blank=True)
    expression = models.CharField(max_length=200, null=True, choices=EXPRESSIONS)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.likevideo.id)
