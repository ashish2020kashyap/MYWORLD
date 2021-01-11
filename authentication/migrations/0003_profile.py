# Generated by Django 3.0.7 on 2021-01-11 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_auth_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('is_celeb', models.BooleanField(null=True)),
                ('is_premium', models.BooleanField(null=True)),
                ('verification_id', models.FileField(null=True, upload_to='')),
                ('profile_picture', models.FileField(null=True, upload_to='profile_picture/LdEOiAjkKKIu1cXtKPBR3Vjj6SCz8SVv')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
