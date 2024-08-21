# Generated by Django 5.1 on 2024-08-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='account',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]