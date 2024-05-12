# Generated by Django 4.0.4 on 2022-06-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('type', models.CharField(blank=True, choices=[('U', 'Universidad'), ('P', 'Preparatoria')], max_length=1, null=True)),
                ('region', models.CharField(blank=True, choices=[('N', 'Norte'), ('CN', 'Centro Norte'), ('C', 'Centro'), ('S', 'Sur')], max_length=2, null=True)),
                ('municipality', models.CharField(blank=True, max_length=50, null=True, verbose_name='Municipio')),
                ('locality', models.CharField(blank=True, max_length=50, null=True, verbose_name='Localidad')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
            ],
        ),
    ]
