from django.db import models

# Create your models here.
class marks(models.Model):
    name = models.CharField(max_length=250)
    mark2 = models.IntegerField()
    garde = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class details(models.Model):
    std=models.CharField(max_length=250)
    address=models.CharField(max_length=500)
    phone=models.IntegerField()
    def __str__(self):
        return self.std
