# Generated by Django 5.0.6 on 2024-06-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_remove_meals_people_remove_meals_preperation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='description',
            field=models.TextField(),
        ),
    ]
