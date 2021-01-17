from django.db import models
from authentication.models import User

from Videos.models import Upload,ChunkUpload
from Like.models import Like
from Comment.models import Comment




class Recommendation(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='userdetails')
    video = models.ForeignKey(Upload, null=True, on_delete=models.SET_NULL, related_name='videodetails')
    chunk = models.ForeignKey(ChunkUpload, null=True, on_delete=models.SET_NULL, related_name='ChunkUpdetails')
    like = models.ForeignKey(Like, null=True, on_delete=models.SET_NULL, related_name='likedetails')
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL, related_name='commentdetails')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user.id)


