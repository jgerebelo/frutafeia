# Generated by Django 3.2.2 on 2021-06-16 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_disponibilidade_medida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='data',
        ),
    ]
