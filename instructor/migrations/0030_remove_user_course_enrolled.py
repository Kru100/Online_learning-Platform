# Generated by Django 4.1.5 on 2023-06-29 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0029_course_enrolled_user_course_enrolled_user_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='course_enrolled',
        ),
    ]
