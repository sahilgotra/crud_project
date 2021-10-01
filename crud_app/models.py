from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  zipcode = models.IntegerField()
  