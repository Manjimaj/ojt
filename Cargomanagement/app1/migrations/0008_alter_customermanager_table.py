# Generated by Django 4.2.1 on 2023-05-26 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_customermanager_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customermanager',
            table='customer',
        ),
    ]
