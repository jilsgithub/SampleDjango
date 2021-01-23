# Generated by Django 3.0.2 on 2020-01-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stname', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=10)),
                ('mark', models.IntegerField(default=50)),
            ],
        ),
    ]
