# Generated by Django 5.1 on 2024-10-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_alter_address_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceRajaOngkir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nama Provinsi')),
            ],
        ),
    ]
