# Generated by Django 5.0.2 on 2024-02-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
