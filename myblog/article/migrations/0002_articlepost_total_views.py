# Generated by Django 3.2.10 on 2022-02-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
