# Generated by Django 5.0.6 on 2024-06-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='media/%Y/%m/%d/')),
                ('facebookLink', models.URLField(max_length=100)),
                ('TwitterLink', models.URLField(max_length=100)),
                ('googlePlusLink', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]