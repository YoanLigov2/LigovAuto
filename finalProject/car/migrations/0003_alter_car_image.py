# Generated by Django 4.2.3 on 2023-08-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(upload_to='images/cars'),
        ),
    ]
