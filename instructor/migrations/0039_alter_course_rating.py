# Generated by Django 4.1.3 on 2023-07-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0038_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=1.0),
        ),
    ]
