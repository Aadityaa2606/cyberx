# Generated by Django 4.2.1 on 2023-05-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_alter_adbstatus_connec_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='screenshot',
            field=models.BooleanField(default=False),
        ),
    ]