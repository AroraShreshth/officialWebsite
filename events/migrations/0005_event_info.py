# Generated by Django 2.2.5 on 2020-02-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200207_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
