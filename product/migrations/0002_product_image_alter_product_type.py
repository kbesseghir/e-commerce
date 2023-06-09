# Generated by Django 4.1.7 on 2023-03-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('velo', 'velo'), ('e-velo', 'velo electrique'), ('e-scotter', 'scotter electrique'), ('Accesoires', 'Accesoires')], max_length=255),
        ),
    ]
