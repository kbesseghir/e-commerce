# Generated by Django 4.1.7 on 2023-03-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=255, unique=True),
        ),
    ]
