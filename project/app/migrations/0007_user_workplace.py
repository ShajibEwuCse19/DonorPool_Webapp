# Generated by Django 4.0.5 on 2022-08-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='workplace',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]