# Generated by Django 4.0 on 2021-12-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='null', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
