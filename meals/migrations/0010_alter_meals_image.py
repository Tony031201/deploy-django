# Generated by Django 5.0.6 on 2024-07-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0009_alter_meals_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='meals/'),
        ),
    ]