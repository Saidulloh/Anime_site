# Generated by Django 4.0.5 on 2022-06-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=10),
        ),
    ]
