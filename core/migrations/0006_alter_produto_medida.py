# Generated by Django 3.2.2 on 2021-05-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210527_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='medida',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Unidade'), (2, 'Kg')], null=True),
        ),
    ]
