# Generated by Django 4.2 on 2023-04-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230403_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='freights',
            name='Active',
            field=models.BooleanField(default=True, verbose_name='Есть на сайте'),
        ),
    ]
