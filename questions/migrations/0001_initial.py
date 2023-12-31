# Generated by Django 4.2.4 on 2023-08-26 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=5000)),
                ('level', models.CharField(max_length=20)),
                ('approach', models.CharField(max_length=50000)),
                ('solution', models.CharField(max_length=50000)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2023, 8, 26, 16, 37, 38, 456582))),
            ],
        ),
    ]
