# Generated by Django 5.0.3 on 2024-03-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Treino_tempo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tempo_real', models.CharField(max_length=100)),
                ('tempo_exato', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]