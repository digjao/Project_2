# Generated by Django 3.2.3 on 2021-08-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('initialBid', models.FloatField()),
                ('image', models.URLField()),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]