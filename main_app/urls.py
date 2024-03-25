from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('people/', views.people_index, name='index'),
    path('people/<int:person_id>/', views.people_detail, name='detail'),
    path('people/create/', views.PersonCreate.as_view(), name='people_create'),
    path('people/<int:pk>/update/', views.PersonUpdate.as_view(), name='people_update'),
    path('people/<int:pk>/delete/', views.PersonDelete.as_view(), name='people_delete'),
    path('People/<int:person_id>/add_carwash/', views.add_carwash, name='add_carwash'),
    path('people/<int:person_id>/assoc_vehicle/<int:vehicle_id>/', views.assoc_vehicle, name='assoc_vehicle'),
]