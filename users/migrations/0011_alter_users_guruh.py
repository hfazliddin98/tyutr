# Generated by Django 5.1.6 on 2025-02-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_users_guruh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='guruh',
            field=models.ManyToManyField(blank=True, related_name='guruh', to='users.guruh'),
        ),
    ]
