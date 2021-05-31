# Generated by Django 3.2.2 on 2021-05-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_student_self_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_homework',
            fields=[
                ('ms_num', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('Requirement', models.TextField()),
                ('subject', models.CharField(max_length=256)),
                ('published_time', models.DateField(auto_now=True)),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
