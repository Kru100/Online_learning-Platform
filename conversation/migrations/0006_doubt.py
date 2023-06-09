# Generated by Django 4.1.5 on 2023-06-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('doubt', models.CharField(max_length=1000)),
                ('rcv', models.EmailField(max_length=254)),
                ('reply', models.TextField()),
                ('course', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('is_replied', models.BooleanField(default=False)),
            ],
        ),
    ]
