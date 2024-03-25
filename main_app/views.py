from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Person, Vehicle
from .forms import Car_WashForm

def home(request):
    return render(request, 'home.html')

def explore(request):
    return render(request, 'explore.html')

def people_index(request):
    people = Person.objects.all()
    return render(request, 'people/index.html', {
        'people': people
    })

def people_detail(request, person_id):
    person = Person.objects.get(id=person_id)
    id_list = person.vehicles.all().values_list('id')
    vehicles_person_doesnt_have = Vehicle.objects.exclude(id__in=id_list)
    carwash_form = Car_WashForm()
    return render(request, 'people/detail.html', 
                  { 'person': person, 
                    'carwash_form': carwash_form,
                    'vehicles': vehicles_person_doesnt_have
                  })

class PersonCreate(CreateView):
    model = Person
    fields = ['image', 'name', 'age', 'description']
    
    def get_success_url(self):
        return '/people/{}/'.format(self.object.id)

class PersonUpdate(UpdateView):
    model = Person
    fields = ['description', 'age']

class PersonDelete(DeleteView):
    model = Person
    success_url = '/people'

def add_carwash(request, person_id):
    form = Car_WashForm(request.POST)
    if form.is_valid():
        new_carwash = form.save(commit=False)
        new_carwash.person_id = person_id
        new_carwash.save()
    return redirect('detail', person_id=person_id)

class VehicleList(ListView):
  model = Vehicle

class VehicleDetail(DetailView):
  model = Vehicle

class VehicleCreate(CreateView):
  model = Vehicle
  fields = '__all__'

class VehicleUpdate(UpdateView):
  model = Vehicle
  fields = ['make', 'model', 'year', 'color']

class VehicleDelete(DeleteView):
  model = Vehicle
  success_url = '/vehicles'


def assoc_vehicle(request, person_id, vehicle_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Person.objects.get(id=person_id).vehicles.add(vehicle_id)
  return redirect('detail', person_id=person_id)

def unassoc_vehicle(request, person_id, vehicle_id):
  Person.objects.get(id=person_id).vehicles.remove(vehicle_id)
  return redirect('detail', person_id=person_id)