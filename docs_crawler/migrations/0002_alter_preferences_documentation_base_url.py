# Generated by Django 3.2.18 on 2023-11-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs_crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='documentation_base_url',
            field=models.CharField(default='https://documentation', max_length=512),
        ),
    ]
