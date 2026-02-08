from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment, MedicalRecord
import json


def index(request):
    """Main dashboard view"""
    patients_count = Patient.objects.count()
    doctors_count = Doctor.objects.count()
    appointments_count = Appointment.objects.count()
    
    context = {
        'patients_count': patients_count,
        'doctors_count': doctors_count,
        'appointments_count': appointments_count,
    }
    return render(request, 'clinic/index.html', context)


@login_required
def patients_list(request):
    """View to list all patients"""
    patients = Patient.objects.all()
    context = {
        'patients': patients
    }
    return render(request, 'clinic/patients_list.html', context)


@login_required
def patient_detail(request, patient_id):
    """View to show patient details"""
    patient = get_object_or_404(Patient, patient_id=patient_id)
    medical_records = MedicalRecord.objects.filter(patient=patient)
    appointments = Appointment.objects.filter(patient=patient)
    
    context = {
        'patient': patient,
        'medical_records': medical_records,
        'appointments': appointments
    }
    return render(request, 'clinic/patient_detail.html', context)


@login_required
def doctors_list(request):
    """View to list all doctors"""
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'clinic/doctors_list.html', context)


@login_required
def appointments_list(request):
    """View to list all appointments"""
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    context = {
        'appointments': appointments
    }
    return render(request, 'clinic/appointments_list.html', context)


@login_required
def appointment_detail(request, appointment_id):
    """View to show appointment details"""
    appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
    context = {
        'appointment': appointment
    }
    return render(request, 'clinic/appointment_detail.html', context)


@login_required
def medical_records_list(request):
    """View to list all medical records"""
    medical_records = MedicalRecord.objects.select_related('patient', 'doctor').all()
    context = {
        'medical_records': medical_records
    }
    return render(request, 'clinic/medical_records_list.html', context)
