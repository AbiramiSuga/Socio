# Generated by Django 4.0.2 on 2023-04-08 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='reqreceiver_id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='reqsender_id',
        ),
        migrations.DeleteModel(
            name='chat',
        ),
        migrations.DeleteModel(
            name='request',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
