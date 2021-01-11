# Generated by Django 3.1.3 on 2020-12-21 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Videos', '0002_auto_20201208_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('likeuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likeuser', to=settings.AUTH_USER_MODEL)),
                ('likevideo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='likevideo', to='Videos.upload')),
            ],
        ),
    ]
