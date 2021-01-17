from django.db import models
from authentication.models import User
from Videos.models import Upload


class Comment(models.Model):
    commentuser = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='commentuser')
    commentvideo = models.ForeignKey(Upload, null=True, on_delete=models.SET_NULL, related_name='commentvideo')
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.commentvideo.id)
