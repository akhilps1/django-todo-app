# Generated by Django 4.1.1 on 2022-10-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='completed',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
