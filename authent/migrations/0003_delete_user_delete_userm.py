# Generated by Django 4.1.5 on 2023-06-29 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0026_remove_course_enrolled'),
        ('authent', '0002_userm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserM',
        ),
    ]