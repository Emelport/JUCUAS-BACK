# Generated by Django 4.0.4 on 2024-01-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0005_reviewer_origin_highschool'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='reviewer_permission',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Permisos'),
        ),
    ]
