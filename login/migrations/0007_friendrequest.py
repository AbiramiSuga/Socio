# Generated by Django 4.1.7 on 2023-04-10 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_friends1'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.user')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender1', to='login.user')),
            ],
        ),
    ]
