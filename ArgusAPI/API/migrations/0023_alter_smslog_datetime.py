# Generated by Django 4.2.1 on 2023-07-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0022_calllog_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslog',
            name='datetime',
            field=models.CharField(max_length=100),
        ),
    ]
