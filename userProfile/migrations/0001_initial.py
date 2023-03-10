# Generated by Django 3.1 on 2022-12-06 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.CharField(blank=True, max_length=30, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('objective', models.TextField()),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('education', models.CharField(blank=True, max_length=200, null=True)),
                ('certification', models.CharField(blank=True, max_length=200, null=True)),
                ('skills', models.CharField(blank=True, max_length=200, null=True)),
                ('data_base', models.CharField(blank=True, max_length=200, null=True)),
                ('programming_laung', models.CharField(blank=True, max_length=200, null=True)),
                ('others', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('current_designation', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('projects', models.CharField(blank=True, max_length=100, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.peron')),
            ],
        ),
    ]
