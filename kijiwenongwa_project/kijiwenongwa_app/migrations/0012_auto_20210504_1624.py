# Generated by Django 3.0.4 on 2021-05-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kijiwenongwa_app', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Phone_number',
            field=models.IntegerField(blank=True, max_length=13, null=True),
        ),
    ]