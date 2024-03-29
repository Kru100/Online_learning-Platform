# Generated by Django 4.1.5 on 2023-07-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0043_alter_course_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('payment_id', models.CharField(max_length=150)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
