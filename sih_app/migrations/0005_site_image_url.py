# Generated by Django 4.0.3 on 2022-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0004_alter_user_aadhaar_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='image_url',
            field=models.CharField(default='https://source.unsplash.com/1920x1080/?nature', max_length=300),
        ),
    ]