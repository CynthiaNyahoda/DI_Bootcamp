from django.db import models

# Create your models here.
from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
def animals(self):
        return Animal.objects.filter(family_id=self.id)
    
    
class Animal(models.Model):
    name = models.CharField(max_length=100)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
