# Generated by Django 5.0.1 on 2024-02-25 16:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piapp', '0004_rename_userprofile_usersprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UsersProfile',
            new_name='Profile',
        ),
    ]
