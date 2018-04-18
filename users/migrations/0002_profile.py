# Generated by Django 2.0.4 on 2018-04-17 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_general_handyman', models.BooleanField(default=False)),
                ('general_handyman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tasker')),
            ],
        ),
    ]