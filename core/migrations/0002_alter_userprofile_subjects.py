# Generated by Django 5.2.1 on 2025-05-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='core.course'),
        ),
    ]
