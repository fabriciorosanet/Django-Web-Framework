# Generated by Django 4.2.16 on 2024-11-24 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autores', '0001_initial'),
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autores',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='autores.autores'),
            preserve_default=False,
        ),
    ]
