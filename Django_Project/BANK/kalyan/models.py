from django.db import models

# Create your models here.
class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()


    def __str__(self):
        return self.website