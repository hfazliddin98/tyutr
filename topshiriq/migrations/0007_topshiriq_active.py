# Generated by Django 5.1.4 on 2025-02-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0006_alter_majburiytopshiriq_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topshiriq',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
