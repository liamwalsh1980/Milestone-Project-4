# Generated by Django 3.2 on 2022-01-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220106_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_colors',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
