# Generated by Django 3.0.7 on 2021-01-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210111_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.FileField(null=True, upload_to='profile_picture/WfJmi4ojBAzp1fTKUCFlpCezp42M3MPg'),
        ),
    ]