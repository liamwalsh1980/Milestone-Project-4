# Generated by Django 3.2 on 2022-01-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complete', '0002_auto_20220128_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='more_information',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
