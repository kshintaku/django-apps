# Generated by Django 3.1.1 on 2020-10-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20201008_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.TextField(choices=[('breakfast', 'BREAKFAST'), ('lunch', 'LUNCH'), ('dinner', 'DINNER'), ('dessert', 'DESSERT'), ('drink', 'DRINK')], default='DESSERT', editable=False, verbose_name='category'),
        ),
    ]
