from django.db import models

# Create your models here.
class userTable(models.Model):
   username = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   firstName = models.CharField(max_length=200)
   lastName = models.CharField(max_length=200)