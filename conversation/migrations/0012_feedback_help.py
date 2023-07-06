# Generated by Django 4.1.5 on 2023-07-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0011_alter_doubt_ask_doubt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('helpline', models.CharField(max_length=5000)),
                ('is_solve', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]