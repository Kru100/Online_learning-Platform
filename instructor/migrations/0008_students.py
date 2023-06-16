# Generated by Django 4.1.5 on 2023-06-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0007_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
    ]