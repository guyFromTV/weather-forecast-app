# Generated by Django 5.1.6 on 2025-02-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_alter_city_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
