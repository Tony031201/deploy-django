# Generated by Django 5.0.6 on 2024-07-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0010_alter_meals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=1, upload_to='meals/'),
            preserve_default=False,
        ),
    ]
