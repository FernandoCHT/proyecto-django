# Generated by Django 3.2.4 on 2021-08-04 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0011_alter_alumnos_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumnos',
            old_name='imagen',
            new_name='image',
        ),
    ]
