# Generated by Django 4.2.1 on 2023-05-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_alter_branch_branchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branchid',
            field=models.CharField(default='BBID4', max_length=50, primary_key=True, serialize=False),
        ),
    ]
