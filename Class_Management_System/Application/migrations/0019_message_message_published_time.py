# Generated by Django 3.2.2 on 2021-05-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0018_homework_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_message',
            name='published_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
