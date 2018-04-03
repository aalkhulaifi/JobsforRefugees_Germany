# Generated by Django 2.0.4 on 2018-04-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(choices=[('General Handyman', 'General Handyman'), ('Moving and packing', 'Moving and packing'), ('Home improvement', 'Home improvement'), ('Mounting and installation', 'Mounting and installation'), ('Yard work', 'Yard work'), ('Help moving', 'Help moving')], max_length=30, verbose_name='Task choices ')),
            ],
        ),
    ]
