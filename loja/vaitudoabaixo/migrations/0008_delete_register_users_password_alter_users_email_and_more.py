# Generated by Django 4.2.5 on 2023-11-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0007_alter_register_email_alter_register_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
