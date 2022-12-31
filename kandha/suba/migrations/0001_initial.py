# Generated by Django 4.1.3 on 2022-12-14 05:07

from django.db import migrations, models
import django.db.models.deletion
import suba.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('carowner', models.CharField(max_length=100)),
                ('carnumber', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=suba.models.getfilename)),
                ('description', models.TextField(max_length=500)),
                ('submission_date', models.DateTimeField()),
                ('year_old', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('service_image', models.ImageField(blank=True, null=True, upload_to=suba.models.getfilename)),
                ('service_cost', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suba.catagory')),
            ],
        ),
    ]