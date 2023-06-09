# Generated by Django 4.1.2 on 2023-06-08 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rutuser',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='comuna'),
        ),
    ]
