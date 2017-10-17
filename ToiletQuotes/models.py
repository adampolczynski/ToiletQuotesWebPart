from django.db import models

class Quote(models.Model):
    user=models.CharField(max_length=20)
    lang=models.CharField(max_length=5)
    quote=models.CharField(max_length=300)
    category=models.CharField(max_length=10)
