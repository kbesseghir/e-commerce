# Generated by Django 4.1.7 on 2023-04-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=5),
            preserve_default=False,
        ),
    ]
