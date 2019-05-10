# Generated by Django 2.2 on 2019-04-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='agra', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(default='UP', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='zip',
            field=models.IntegerField(default=12345),
            preserve_default=False,
        ),
    ]
