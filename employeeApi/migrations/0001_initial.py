# Generated by Django 3.1.3 on 2020-11-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.TextField(max_length=255)),
                ('lastName', models.TextField(max_length=255)),
                ('phone', models.TextField()),
                ('email', models.TextField(max_length=255)),
            ],
        ),
    ]
