# Generated by Django 4.2.1 on 2023-05-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_rename_booking_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookingid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='customerid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.IntegerField(max_length=50),
        ),
    ]
