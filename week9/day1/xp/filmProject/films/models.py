from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Film(models.Model):
        title = models.CharField(max_length=100)
        release_date = models.DateField()
        created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='film_created')
        available_in_countries = models.ManyToManyField(Country, related_name='Film_available')
        category = models.ManyToManyField(Category)
        director = models.ManyToManyField(Director)
        
        def __str__(self):
            return self.titles
    
