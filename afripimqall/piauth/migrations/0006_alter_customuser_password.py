# Generated by Django 5.0.1 on 2024-03-04 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piauth', '0005_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
