# Generated by Django 4.2.5 on 2023-11-15 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0015_myuser_groups_myuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
