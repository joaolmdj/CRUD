# Generated by Django 3.1.7 on 2021-03-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
