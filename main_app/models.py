from django.db import models
from django.urls import reverse


# Create your models here.
class Vehicle(models.Model):
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.model

  def get_absolute_url(self):
    return reverse('vehicles_detail', kwargs={'pk': self.id})

class Person(models.Model):
    image = models.ImageField(upload_to='images/', default='2/static/images/blank-car-Photoroom.png')
    name = models.CharField(max_length=100, default='Mystery')
    age = models.IntegerField()
    description = models.CharField(max_length=2000, default='No Description')
    vehicles = models.ManyToManyField(Vehicle)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'person_id': self.id})
    

class CarWash(models.Model):
    date=models.DateField('Date of Car Wash')
                           
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.date}"
    
class Meta:
    ordering = ['-date']


 