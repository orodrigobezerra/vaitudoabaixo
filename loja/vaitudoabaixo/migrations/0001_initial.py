# Generated by Django 4.2.7 on 2023-11-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('color', models.TextField(max_length=50)),
                ('instrument', models.TextField(max_length=200)),
                ('qty_stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=2, max_length=20)),
                ('image', models.URLField()),
            ],
        ),
    ]