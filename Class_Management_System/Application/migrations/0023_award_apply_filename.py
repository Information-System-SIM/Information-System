# Generated by Django 3.2.2 on 2021-05-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0022_award_apply_uploaded_stu'),
    ]

    operations = [
        migrations.AddField(
            model_name='award_apply',
            name='filename',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]