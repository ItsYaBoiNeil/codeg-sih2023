from django.db import models

# Create your models here.
class submittedURLs(models.Model):
    url = models.CharField(max_length=200)
    output = models.BooleanField()