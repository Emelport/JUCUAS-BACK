# Generated by Django 4.0.4 on 2022-08-21 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('representative', '0002_representative_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='representative_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
