# Generated by Django 5.0.1 on 2024-03-04 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piauth', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
