from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from people.models import Person

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

for p in people:
    person = Person(id=p['id'], name=p['name'], age=p['age'], country=p['country'])
    person.save()
