# Generated by Django 4.1.5 on 2023-06-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0002_course_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('qualification', models.TextField()),
                ('is_registered', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_instructor', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=64)),
                ('otp', models.IntegerField(default=0)),
                ('token', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
