# Generated by Django 4.0.5 on 2022-06-17 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
