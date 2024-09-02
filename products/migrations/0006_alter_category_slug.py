# Generated by Django 5.1 on 2024-09-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_slug_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, editable=False, max_length=50, unique=True, verbose_name='Content Slug'),
        ),
    ]
