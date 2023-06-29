# Generated by Django 4.1.5 on 2023-06-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0007_delete_doubt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doubt_ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('sender', models.EmailField(max_length=254)),
                ('doubt', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('is_replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doubt_replied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('ask_id', models.IntegerField()),
                ('receiver', models.EmailField(max_length=254)),
                ('reply', models.CharField(max_length=2500)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
