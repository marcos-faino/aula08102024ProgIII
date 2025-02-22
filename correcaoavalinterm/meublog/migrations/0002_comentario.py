# Generated by Django 3.1.7 on 2022-05-09 19:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meublog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('corpo', models.TextField(verbose_name='Comentário')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('atualizado', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meublog.post')),
            ],
            options={
                'verbose_name': 'Comentário',
                'verbose_name_plural': 'Comentários',
                'ordering': ('-criado',),
            },
        ),
    ]
