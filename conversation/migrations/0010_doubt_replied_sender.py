# Generated by Django 4.1.5 on 2023-07-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0009_doubt_ask_reply_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubt_replied',
            name='sender',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]