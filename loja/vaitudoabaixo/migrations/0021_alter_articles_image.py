# Generated by Django 4.2.5 on 2023-11-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0020_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.TextField(),
        ),
    ]
