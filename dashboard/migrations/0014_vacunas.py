# Generated by Django 4.0.3 on 2022-05-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_order_nombre_de_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_vacuna', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Vacunas',
            },
        ),
    ]
