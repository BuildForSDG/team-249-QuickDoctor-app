# Generated by Django 3.0.6 on 2020-05-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200512_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='doctor',
        ),
    ]