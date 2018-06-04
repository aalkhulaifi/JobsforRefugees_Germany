# Generated by Django 2.0.4 on 2018-06-04 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_auto_20180527_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('contact_number', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Denied', 'Denied'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('tasker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tasker')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]