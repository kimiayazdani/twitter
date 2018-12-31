# Generated by Django 2.1.3 on 2018-12-30 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='twitterApp.Profile')),
            ],
        ),
    ]