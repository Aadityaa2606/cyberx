# Generated by Django 4.2.1 on 2023-05-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0020_alter_smslog_sms_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='exif_date_time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]