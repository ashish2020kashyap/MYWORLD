# Generated by Django 3.0.7 on 2021-01-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210111_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.FileField(null=True, upload_to='profile_picture/8bw0QLTW4CJjU6PkLuMO993D1JyTOKkj'),
        ),
    ]
