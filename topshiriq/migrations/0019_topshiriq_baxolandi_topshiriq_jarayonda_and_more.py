# Generated by Django 5.1.6 on 2025-02-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0018_alter_majburiytopshiriq_tur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topshiriq',
            name='baxolandi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topshiriq',
            name='jarayonda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topshiriq',
            name='vaqt_tugadi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topshiriq',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
