from django.db import models

# Create your models here.

class TextForCryptoModel(models.Model):
    text = models.TextField(max_length=1000)
    crypted_text = models.TextField(max_length=1000)


