# Generated by Django 4.0.4 on 2024-01-23 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_alter_university_type'),
        ('reviewer', '0004_reviewer_global_reviewer_reviewer_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='origin_highschool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_highschool', to='university.university'),
        ),
    ]
