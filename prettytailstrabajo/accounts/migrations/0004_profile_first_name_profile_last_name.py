# Generated by Django 4.1.2 on 2023-06-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_rutuser_profile_rut_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Apellidos'),
        ),
    ]
