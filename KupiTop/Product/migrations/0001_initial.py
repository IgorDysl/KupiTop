# Generated by Django 2.2.20 on 2021-05-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=20)),
                ('short_disc', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True)),
                ('discount', models.BooleanField()),
                ('photo', models.FileField(upload_to='img/')),
            ],
        ),
    ]
