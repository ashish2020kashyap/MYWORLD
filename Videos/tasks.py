from celery import shared_task

from time import sleep
from .models import *
from django.contrib.auth.models import User
from .serializers import UploadSerializer

import subprocess
import requests
import json









@shared_task
def sleepy(duration):

    sleep(duration)
    sleep(0.1)
    return None


@shared_task
def videoupload(user,title,uploaded_file_url):

    print(user)
    print(title)
    print(uploaded_file_url)
    #id = User.objects.get(id=user)

    contact = Upload(title=title,upload_file=uploaded_file_url)
    contact.save()

    return None










@shared_task
def preprocess(videos_id):
    video_obj=Upload.objects.get(id=videos_id)
    print(videos_id)
    print(video_obj.title)
    print(video_obj.upload_file)
    name=video_obj.upload_file
    video_id = videos_id
    video_name = name
    url = 'https://d6c8rd47z7.execute-api.us-east-1.amazonaws.com/v1/process?video_id={}&video_name={}'.format(video_id,
                                                                                                               video_name)
    p = requests.post(url, data={}, headers={'InvocationType': 'Event'})

    print(p)

    return None


