# Generated by Django 3.1.2 on 2020-11-20 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField(choices=[('incomplete', 'INCOMPLETE'), ('paused', 'PAUSED'), ('complete', 'COMPLETE')], default='incomplete', verbose_name='status')),
                ('complete', models.BinaryField(verbose_name='complete')),
            ],
        ),
    ]
