# Generated by Django 4.2 on 2023-05-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_empleado_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='fecha',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
