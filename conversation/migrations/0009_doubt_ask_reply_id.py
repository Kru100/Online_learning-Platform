# Generated by Django 4.1.5 on 2023-07-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0008_doubt_ask_doubt_replied'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubt_ask',
            name='reply_id',
            field=models.IntegerField(default=None),
        ),
    ]
