# Generated by Django 3.2.4 on 2021-07-20 00:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_alter_comentario_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='image',
        ),
        migrations.AddField(
            model_name='alumnos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='coment',
            field=ckeditor.fields.RichTextField(verbose_name='Comentario'),
        ),
    ]
