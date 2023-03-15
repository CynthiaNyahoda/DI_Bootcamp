from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 

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
