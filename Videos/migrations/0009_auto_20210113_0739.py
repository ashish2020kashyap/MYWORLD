# Generated by Django 3.0.7 on 2021-01-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videos', '0008_auto_20210109_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='category',
            field=models.CharField(blank=True, choices=[('1', 'Film and animation'), ('2', 'Cars and vehicles'), ('3', 'Music'), ('4', 'Pets and animals'), ('5', 'Sport'), ('6', 'Travel and events'), ('7', 'Gaming'), ('8', 'People and blogs'), ('9', 'Comedy'), ('10', 'Entertainment'), ('11', 'News and politics'), ('12', 'How-to and style'), ('13', 'Education'), ('14', 'Science and technology'), ('15', 'Non-profits and activism')], max_length=200, null=True),
        ),
    ]