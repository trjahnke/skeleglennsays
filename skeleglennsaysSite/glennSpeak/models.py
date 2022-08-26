from django.db import models
from django_cryptography.fields import encrypt


class Quotes(models.Model):
    quote_id = models.AutoField(primary_key=True, null=False)
    quote = models.CharField(max_length=150)
    tweeted = models.BooleanField(default=False)
    tweet_date = models.DateTimeField(blank=True, null=True)
    tweet_link = models.URLField(max_length=150, null=True, blank=True)


class TokenHoken(models.Model):
    consumerKey = encrypt(models.CharField(max_length=150))
    consumerSecret = encrypt(models.CharField(max_length=150))
    accessToken = encrypt(models.CharField(max_length=150))
    accessSecret = encrypt(models.CharField(max_length=150))
