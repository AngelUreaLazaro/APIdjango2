# Generated by Django 3.2.4 on 2023-10-20 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_datosimportados_datosformulario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DatosFormulario',
            new_name='DatosCSV',
        ),
    ]
