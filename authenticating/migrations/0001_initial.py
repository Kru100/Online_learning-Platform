# Generated by Django 4.1.5 on 2023-06-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Quiz_id', models.IntegerField()),
                ('question', models.TextField()),
                ('opt1', models.CharField(max_length=100)),
                ('opt2', models.CharField(max_length=100)),
                ('opt3', models.CharField(max_length=100)),
                ('opt4', models.CharField(max_length=100)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]