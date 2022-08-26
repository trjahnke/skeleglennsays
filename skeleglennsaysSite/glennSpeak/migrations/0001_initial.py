# Generated by Django 4.0.6 on 2022-08-03 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('quote_id', models.AutoField(primary_key=True, serialize=False)),
                ('quote', models.CharField(max_length=150)),
                ('tweeted', models.BooleanField(default=False)),
                ('tweet_date', models.DateTimeField(blank=True, null=True)),
                ('tweet_link', models.URLField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
