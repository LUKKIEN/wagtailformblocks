# Generated by Django 1.10.2 on 2016-10-28 12:21
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailformblocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseform',
            name='add_recaptcha',
            field=models.BooleanField(default=False, help_text='Add a reCapcha field to the form.'),
        ),
    ]
