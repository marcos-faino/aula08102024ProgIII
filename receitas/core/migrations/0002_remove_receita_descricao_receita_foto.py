# Generated by Django 4.2.12 on 2024-12-21 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='descricao',
        ),
        migrations.AddField(
            model_name='receita',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto da Receita'),
        ),
    ]
