# Generated by Django 4.1.7 on 2023-03-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('velo', 'velo'), ('e-velo', 'velo electrique'), ('e-scotter', 'scotter electrique'), ('Accesoires', 'Accesoires')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
