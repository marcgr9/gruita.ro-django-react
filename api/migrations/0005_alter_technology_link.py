# Generated by Django 3.2.7 on 2021-09-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210924_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='link',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
