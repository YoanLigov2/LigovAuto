# Generated by Django 4.2.3 on 2023-08-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='image_url',
            field=models.ImageField(upload_to='images/trucks'),
        ),
    ]
