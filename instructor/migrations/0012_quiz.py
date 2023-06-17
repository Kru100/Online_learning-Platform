# Generated by Django 4.1.5 on 2023-06-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0011_delete_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('quiz_id', models.IntegerField()),
                ('question', models.CharField(max_length=500)),
                ('opt1', models.CharField(max_length=250)),
                ('opt2', models.CharField(max_length=250)),
                ('opt3', models.CharField(max_length=250)),
                ('opt4', models.CharField(max_length=250)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
