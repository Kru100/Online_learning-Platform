# Generated by Django 4.1.3 on 2023-07-08 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0039_alter_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
