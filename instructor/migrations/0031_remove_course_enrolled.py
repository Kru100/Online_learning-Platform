# Generated by Django 4.1.5 on 2023-06-29 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0030_remove_user_course_enrolled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled',
        ),
    ]
