# Generated by Django 3.1 on 2022-12-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_auto_20221206_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='peron',
            name='degree_long_form',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
