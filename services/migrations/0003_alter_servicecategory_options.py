# Generated by Django 3.2 on 2022-01-06 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_service_category_servicecategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicecategory',
            options={'verbose_name_plural': 'Service Categories'},
        ),
    ]