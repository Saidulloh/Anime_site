# Generated by Django 4.0.5 on 2022-06-17 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_remove_comment_email_remove_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comm_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
