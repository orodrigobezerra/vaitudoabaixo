# Generated by Django 4.2.5 on 2023-11-15 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0016_othermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othermodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]