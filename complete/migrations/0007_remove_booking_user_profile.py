# Generated by Django 3.2 on 2022-02-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complete', '0006_alter_bookinglineitem_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user_profile',
        ),
    ]
