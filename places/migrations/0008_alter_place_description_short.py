# Generated by Django 5.0.7 on 2024-08-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_remove_place_place_place_description_long_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]