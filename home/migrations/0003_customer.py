# Generated by Django 4.1.7 on 2023-04-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('desc', models.TextField(max_length=100)),
                ('pic', models.ImageField(upload_to='pics')),
            ],
        ),
    ]