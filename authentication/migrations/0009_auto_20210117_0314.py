# Generated by Django 3.0.7 on 2021-01-17 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210113_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_picture/vbcUy2wMkK4551LVDLVDF3FgB5t6jejA'),
        ),
    ]
