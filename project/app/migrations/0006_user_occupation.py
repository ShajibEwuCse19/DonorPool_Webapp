# Generated by Django 4.0.5 on 2022-08-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(choices=[('Student', 'Student'), ('Doctor', 'Doctor'), ('Engineer', 'Engineer')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
