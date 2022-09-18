# Generated by Django 4.0.2 on 2022-09-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.URLField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
