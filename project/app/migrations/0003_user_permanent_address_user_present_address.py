# Generated by Django 4.0.5 on 2022-08-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_gender_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permanent_address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='present_address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
