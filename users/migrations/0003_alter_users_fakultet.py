# Generated by Django 5.1.4 on 2025-02-01 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_fakultets_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='fakultet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.fakultets'),
        ),
    ]
