# Generated by Django 3.0.7 on 2021-01-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210113_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_celeb',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_premium',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='verification_id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_picture/QJOfI7hDPKk2CznV7gyXmuiKJMxHVdP9'),
        ),
    ]
