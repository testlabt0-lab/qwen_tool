from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'gender', 'phone_number', 'email']
    search_fields = ['patient_id', 'first_name', 'last_name', 'phone_number']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'get_full_name', 'specialization', 'phone_number']
    search_fields = ['doctor_id', 'user__first_name', 'user__last_name', 'specialization']

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Full Name'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment_id', 'patient', 'doctor', 'appointment_date', 'status']
    list_filter = ['status', 'appointment_date']
    search_fields = ['appointment_id', 'patient__first_name', 'patient__last_name', 'doctor__user__first_name']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'created_at', 'diagnosis']
    list_filter = ['created_at']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis']
