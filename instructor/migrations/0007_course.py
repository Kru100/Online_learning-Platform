# Generated by Django 4.1.5 on 2023-06-08 14:25

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0006_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instructor', models.EmailField(max_length=254)),
                ('enrolled', djongo.models.fields.ArrayReferenceField(default=None, on_delete=django.db.models.deletion.CASCADE, to='instructor.user')),
            ],
        ),
    ]
