# Generated by Django 3.1.1 on 2020-10-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_recipe_img_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="img_url",
            field=models.CharField(max_length=100, verbose_name="image url"),
        ),
    ]
