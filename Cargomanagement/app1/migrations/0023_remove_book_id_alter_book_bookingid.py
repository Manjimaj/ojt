# Generated by Django 4.2.1 on 2023-05-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_alter_book_bookingid_alter_book_customerid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='bookingid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
