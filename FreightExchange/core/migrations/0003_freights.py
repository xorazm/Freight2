# Generated by Django 3.2.18 on 2023-04-02 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20230402_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weight', models.CharField(max_length=50)),
                ('Comment', models.CharField(max_length=500)),
                ('SubmitedDate', models.DateField()),
                ('Contact', models.CharField(max_length=100)),
                ('TLLink', models.CharField(max_length=100)),
                ('FromLoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromloc', to='core.geolocations')),
                ('ToLoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toloc', to='core.geolocations')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
