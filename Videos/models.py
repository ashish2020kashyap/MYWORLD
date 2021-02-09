from django.db import models
from authentication.models import User
# Create your models here.


class Upload(models.Model):
    CATEGORIES = (
        ('1', 'Film and animation'),
        ('2', 'Cars and vehicles'),
        ('3', 'Music'),
        ('4', 'Pets and animals'),
        ('5', 'Sport'),
        ('6', 'Travel and events'),
        ('7', 'Gaming'),
        ('8', 'People and blogs'),
        ('9', 'Comedy'),
        ('10', 'Entertainment'),
        ('11', 'News and politics'),
        ('12', 'How-to and style'),
        ('13', 'Education'),
        ('14', 'Science and technology'),
        ('15', 'Non-profits and activism'),

    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user')
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES, blank=True)
    upload_file = models.FileField(upload_to='Videos', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ChunkUpload(models.Model):
    video_id = models.OneToOneField(Upload, to_field='id', on_delete=models.CASCADE, null=True, blank=True)
    video_length = models.CharField(max_length=50, null=True, blank=True)
    thumbnail = models.CharField(max_length=1000, null=True, blank=True)
    chunk1 = models.CharField(max_length=1000, null=True, blank=True)
    chunk2 = models.CharField(max_length=1000, null=True, blank=True)
    chunk3 = models.CharField(max_length=1000, null=True, blank=True)
    chunk4 = models.CharField(max_length=1000, null=True, blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.video_id.id)



class IPS(models.Model):
    video = models.ForeignKey(ChunkUpload, null=True, on_delete=models.SET_NULL, related_name='chunkvideo')
    user = models.TextField(default=None)

    def __str__(self):
        return self.user