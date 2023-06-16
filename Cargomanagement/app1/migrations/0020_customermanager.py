# Generated by Django 4.2.1 on 2023-05-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_delete_customermanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customermanager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.IntegerField()),
                ('doornumber', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('emailid', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('mobilenumber', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Ctable',
            },
        ),
    ]