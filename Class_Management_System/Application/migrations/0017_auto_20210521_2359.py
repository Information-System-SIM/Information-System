# Generated by Django 3.2.2 on 2021-05-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0016_auto_20210521_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_activity',
            name='ms_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message_competition',
            name='ms_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message_homework',
            name='ms_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='message_message',
            name='ms_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
