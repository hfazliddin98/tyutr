# Generated by Django 5.1.6 on 2025-02-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topshiriq', '0017_alter_topshiriq_topshiriq_turi_testtopshiriq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majburiytopshiriq',
            name='tur',
            field=models.CharField(choices=[('ttjga_tashrif', 'ttjga_tashrif'), ('ijaraga_tashrif', 'ijaraga_tashrif'), ('tutorlik_soati', 'tutorlik_soati'), ('davra_suhbati', 'davra_suhbati'), ('tadbir', 'tadbir'), ('ttjda_tadbir', 'ttjda_tadbir'), ('iqtidorli_talabam', 'iqtidorli_talabam'), ('oilaga_xat', 'oilaga_xat'), ('test', 'test')], max_length=30),
        ),
        migrations.AlterField(
            model_name='topshiriq',
            name='majburiy_topshiriq_turi',
            field=models.CharField(blank=True, choices=[('ttjga_tashrif', 'ttjga_tashrif'), ('ijaraga_tashrif', 'ijaraga_tashrif'), ('tutorlik_soati', 'tutorlik_soati'), ('davra_suhbati', 'davra_suhbati'), ('tadbir', 'tadbir'), ('ttjda_tadbir', 'ttjda_tadbir'), ('iqtidorli_talabam', 'iqtidorli_talabam'), ('oilaga_xat', 'oilaga_xat'), ('test', 'test')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='topshiriq',
            name='topshiriq_turi',
            field=models.CharField(choices=[('majburiy', 'majburiy'), ('qoshimcha', 'qoshimcha')], default='qoshimcha', max_length=30),
        ),
        migrations.DeleteModel(
            name='TestTopshiriq',
        ),
    ]
