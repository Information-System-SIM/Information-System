# Generated by Django 3.2.2 on 2021-05-20 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0008_alter_message_homework_published_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice_homework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ms_num', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Application.message_homework')),
                ('student_num', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Application.student')),
            ],
        ),
    ]
