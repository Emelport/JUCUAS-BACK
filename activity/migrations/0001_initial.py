# Generated by Django 4.0.4 on 2022-08-13 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre')),
                ('is_optional', models.BooleanField(default=False, verbose_name='Opcional')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='activity.typeactivity')),
            ],
        ),
    ]
