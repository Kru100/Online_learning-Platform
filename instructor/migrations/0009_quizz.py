# Generated by Django 4.1.5 on 2023-06-10 07:05

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0008_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('mark', djongo.models.fields.ArrayReferenceField(default=None, on_delete=django.db.models.deletion.CASCADE, to='instructor.students')),
            ],
        ),
    ]
