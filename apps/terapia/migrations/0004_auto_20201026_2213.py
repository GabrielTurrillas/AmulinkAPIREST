# Generated by Django 3.1 on 2020-10-27 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapia', '0003_auto_20201023_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesion',
            name='fechaPago',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='fechaSesion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
