# Generated by Django 3.0.7 on 2021-01-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20210124_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_picture/meamXA5dAHjEkVfaewJwwDCpLquT9hcP'),
        ),
    ]
