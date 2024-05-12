# Generated by Django 4.0.4 on 2022-11-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0020_evidence_observation_alter_activity_activity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='evidence_status',
            field=models.CharField(choices=[('SEND', 'Subido'), ('DUE', 'Pendiente'), ('INC', 'Incompleto'), ('REJECT', 'Rechazado'), ('OK', 'Aprobado')], default='DUE', max_length=6, null=True),
        ),
    ]
