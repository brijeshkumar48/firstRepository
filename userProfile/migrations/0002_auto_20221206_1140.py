# Generated by Django 3.1 on 2022-12-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peron',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
