# Generated by Django 4.1.5 on 2023-06-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
