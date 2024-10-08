# Generated by Django 4.0.4 on 2022-08-21 18:16

import activity.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_manager', '0002_activitymanager_academic_degree'),
        ('presenter', '0004_delete_deadline_remove_presenter_activity_and_more'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_edition', models.DateTimeField(default=2022)),
                ('date_to_upload_activities', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 894264))),
                ('date_to_upload_evidence', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 894274))),
                ('date_to_validate_evidence', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 894282))),
                ('date_edition_start', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 894289))),
                ('end_date_of_the_edition', models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 894295))),
            ],
        ),
        migrations.CreateModel(
            name='TypeEvidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
                ('is_optional', models.BooleanField(default=False, verbose_name='Opcional')),
            ],
        ),
        migrations.RemoveField(
            model_name='typeactivity',
            name='is_optional',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity_manager.activitymanager'),
        ),
        migrations.AddField(
            model_name='activity',
            name='area_knowledge',
            field=models.CharField(choices=[('I', 'I.fisico-matematicas y ciencias de la tierra'), ('II', 'II.Biologia y quimica'), ('III', 'III.Medicina y ciencias de la salud'), ('IV', 'IV.Ciencias de la conducta y la educacion'), ('V', 'V.Humanidades'), ('VI', 'VI.Ciencias sociales'), ('VII', 'VII.Ciencias de agricultura, agropecuarias, forestales y de ecosistemas'), ('VIII', 'VIII.Ingenierias y desarrollo tecnologico')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='co_presenter',
            field=models.ManyToManyField(related_name='co_presenter', to='presenter.presenter'),
        ),
        migrations.AddField(
            model_name='activity',
            name='date_activity',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 21, 12, 16, 18, 892918)),
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descipción'),
        ),
        migrations.AddField(
            model_name='activity',
            name='educational_level_to_is_directed',
            field=models.CharField(blank=True, choices=[('PCO', 'Público en general'), ('PREESC', 'Preescolar'), ('PRIM', 'Primaria'), ('SEC', 'Secundaria'), ('MDSUP', 'Media superior'), ('SUP', 'Superior')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='modality',
            field=models.CharField(blank=True, choices=[('V', 'Virtual'), ('P', 'Presencial')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='numbers_expected_attendees',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Numero de asistentes esperados'),
        ),
        migrations.AddField(
            model_name='activity',
            name='numbers_total_attendees',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Numero de asistentes totales'),
        ),
        migrations.AddField(
            model_name='activity',
            name='presenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='presenter', to='presenter.presenter'),
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre')),
                ('evidence_file', models.FileField(blank=True, null=True, upload_to=activity.models.upload_evidence_file, verbose_name='Archivo')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='activity.activity', verbose_name='Actividad')),
                ('type_evidence', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='activity.typeevidence')),
            ],
        ),
        migrations.AddField(
            model_name='typeactivity',
            name='type_evidence',
            field=models.ManyToManyField(related_name='type_evidence', to='activity.typeevidence'),
        ),
    ]
