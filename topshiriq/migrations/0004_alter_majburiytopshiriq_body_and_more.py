# Generated by Django 5.1.4 on 2025-02-01 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0003_topshiriq_body_topshiriq_file1_topshiriq_file2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majburiytopshiriq',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qoshimchatopshiriq',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topshiriq',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
