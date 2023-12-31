# Generated by Django 4.2.5 on 2023-11-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0006_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='register',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
