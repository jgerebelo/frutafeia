# Generated by Django 3.2.2 on 2021-05-25 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapaDeCampo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('quantidade', models.FloatField()),
                ('medida', models.PositiveSmallIntegerField(choices=[(1, 'Unidade'), (2, 'Kg')])),
                ('preco', models.FloatField()),
                ('urgente', models.BooleanField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produtor')),
            ],
        ),
    ]
