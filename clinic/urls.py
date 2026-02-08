from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.patients_list, name='patients_list'),
    path('patients/<str:patient_id>/', views.patient_detail, name='patient_detail'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/<str:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('medical-records/', views.medical_records_list, name='medical_records_list'),
]