# Generated by Django 2.2 on 2019-04-20 20:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(default=1, on_delete='cascade', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
