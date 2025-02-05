# Generated by Django 3.2.2 on 2021-05-24 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Família de Produto',
                'verbose_name_plural': 'Famílias de Produtos',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Verde'), (2, 'Fruta'), (3, 'Outro')], null=True)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.familiaproduto')),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('estado', models.PositiveSmallIntegerField(choices=[(1, 'Final'), (2, 'Potencial'), (3, 'Antigo'), (3, 'Lista Negra')])),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('morada', models.CharField(blank=True, max_length=255, null=True)),
                ('concelho', models.CharField(blank=True, max_length=255, null=True)),
                ('produtos', models.ManyToManyField(to='core.Produto')),
            ],
            options={
                'verbose_name_plural': 'Produtores',
            },
        ),
        migrations.CreateModel(
            name='Disponibilidade',
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
