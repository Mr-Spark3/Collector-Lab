from django.forms import ModelForm
from .models import CarWash

class Car_WashForm(ModelForm):
  class Meta:
    model = CarWash
    fields = ['date']