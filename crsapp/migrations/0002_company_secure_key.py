# Generated by Django 4.1.7 on 2023-04-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='secure_key',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
