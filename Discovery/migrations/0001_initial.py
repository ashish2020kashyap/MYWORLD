# Generated by Django 3.1.3 on 2020-12-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='none/no-img.jpg', upload_to='')),
            ],
        ),
    ]
