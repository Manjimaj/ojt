# Generated by Django 4.2.1 on 2023-05-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_bookingmanager_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookingmanager',
            table='Booking',
        ),
        migrations.AlterModelTable(
            name='customermanager',
            table='customer',
        ),
    ]
