# Generated by Django 4.0.4 on 2022-09-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_university_acronym'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationalunit',
            name='acronym',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Siglas'),
        ),
    ]
