# Generated by Django 2.1.3 on 2019-01-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterApp', '0004_loggedinuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='allowed_request',
            field=models.BooleanField(default=True),
        ),
    ]
