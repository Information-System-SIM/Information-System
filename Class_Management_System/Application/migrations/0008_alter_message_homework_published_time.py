# Generated by Django 3.2.2 on 2021-05-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0007_message_homework_useable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_homework',
            name='published_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]