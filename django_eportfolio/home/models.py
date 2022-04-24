import email
from django.db import models

# Create your models here.
from django.db import models
#source of info
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()