# Generated by Django 4.1 on 2022-09-02 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dni',
        ),
    ]
