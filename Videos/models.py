from django.db import models
from authentication.models import User
# Create your models here.

class Upload(models.Model):
    CATEGORIES = (
        ('Film and animation', 'Film and animation'),
        ('Cars and vehicles', 'Cars and vehicles'),
        ('Music', 'Music'),
        ('Pets and animals', 'Pets and animals'),
        ('Sport', 'Sport'),
        ('Travel and events', 'Travel and events'),
        ('Gaming', 'Gaming'),
        ('People and blogs', 'People and blogs'),
        ('Comedy', 'Comedy'),
        ('Entertainment', 'Entertainment'),
        ('News and politics', 'News and politics'),
        ('How-to and style', 'How-to and style'),
        ('Education', 'Education'),
        ('Science and technology', 'Science and technology'),
        ('Non-profits and activism', 'Non-profits and activism'),



    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user')
    title = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORIES,blank=True)
    upload_file = models.FileField(upload_to='Videos', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.title






class ChunkUpload(models.Model):
    #video_id = models.ForeignKey(Upload, null=True, on_delete=models.SET_NULL, related_name='upload')
    video_id = models.OneToOneField(Upload, to_field='id', on_delete=models.CASCADE,null = True,blank=True)
    video_length = models.CharField(max_length=50, null=True, blank=True)
    thumbnail = models.CharField(max_length=1000,null=True, blank=True)
    chunk1 = models.CharField(max_length=1000,null=True, blank=True)
    chunk2 = models.CharField(max_length=1000, null=True, blank=True)
    chunk3 = models.CharField(max_length=1000, null=True, blank=True)
    chunk4 = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.thumbnail