# Generated by Django 3.1.7 on 2021-11-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20210818_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='words',
            name='word',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='wrong',
            name='wrong_one',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
