# Generated by Django 4.0.4 on 2022-06-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Mujer'), ('H', 'Hombre'), ('O', 'Otro')], max_length=1, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo')),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
            ],
        ),
    ]
