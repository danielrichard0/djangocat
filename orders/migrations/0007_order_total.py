# Generated by Django 5.1 on 2024-10-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=100000, verbose_name='Harga Keseluruhan Tambah Ongkir'),
            preserve_default=False,
        ),
    ]
