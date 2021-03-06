# Generated by Django 3.0.4 on 2020-03-21 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('fName', models.CharField(max_length=20)),
                ('mName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('cellPhone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('org', models.CharField(max_length=20)),
            ],
        ),
    ]
