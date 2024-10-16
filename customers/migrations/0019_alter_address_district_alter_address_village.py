# Generated by Django 5.1 on 2024-10-08 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0018_alter_address_city_alter_address_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='customers.district'),
        ),
        migrations.AlterField(
            model_name='address',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='customers.villages'),
        ),
    ]
