# Generated by Django 5.1 on 2024-09-23 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_user_alter_cart_session_id'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.session'),
        ),
    ]
