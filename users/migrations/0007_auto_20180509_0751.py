# Generated by Django 2.0.4 on 2018-05-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180509_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasker',
            old_name='tasker',
            new_name='user',
        ),
    ]