# Generated by Django 5.0.2 on 2024-02-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
