# Generated by Django 4.2.5 on 2023-11-06 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaitudoabaixo', '0002_alter_articles_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=50)),
            ],
        ),
    ]
