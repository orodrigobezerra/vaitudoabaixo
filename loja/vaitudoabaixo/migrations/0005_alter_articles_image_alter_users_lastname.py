# Generated by Django 4.2.5 on 2023-11-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0004_users_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.TextField(default='', max_length=100),
        ),
    ]
