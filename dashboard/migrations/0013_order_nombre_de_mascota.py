# Generated by Django 4.0.3 on 2022-05-03 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_order_nombre_de_mascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nombre_de_mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product'),
        ),
    ]
