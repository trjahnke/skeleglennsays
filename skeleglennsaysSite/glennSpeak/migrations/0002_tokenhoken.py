# Generated by Django 4.0.6 on 2022-08-04 00:18

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('glennSpeak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenHoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumerKey', django_cryptography.fields.encrypt(models.CharField(max_length=150))),
                ('consumerSecret', django_cryptography.fields.encrypt(models.CharField(max_length=150))),
                ('accessToken', django_cryptography.fields.encrypt(models.CharField(max_length=150))),
                ('accessSecret', django_cryptography.fields.encrypt(models.CharField(max_length=150))),
            ],
        ),
    ]