from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)

    def __str__(self):
        return self.name