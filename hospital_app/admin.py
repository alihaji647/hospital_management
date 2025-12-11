from django.contrib import admin
from .models import Patient, Doctor, Appointment

# Change admin site header
admin.site.site_header = "🏥 Hospital Management Admin"
admin.site.site_title = "Hospital Admin"
admin.site.index_title = "Welcome to Hospital Management System"

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'registration_date')
    list_filter = ('gender', 'blood_group')
    search_fields = ('first_name', 'last_name', 'email', 'patient_id', 'phone')
    ordering = ('-registration_date',)
    exclude = ('registration_date',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address', 'emergency_contact')
        }),
        ('System Information', {
            'fields': ('patient_id',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'first_name', 'last_name', 'specialization', 'department', 'experience', 'consultation_fee', 'status')
    list_filter = ('specialization', 'department', 'status')
    search_fields = ('first_name', 'last_name', 'specialization', 'doctor_id')
    ordering = ('specialization', 'last_name')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Professional Information', {
            'fields': ('specialization', 'department', 'qualification', 'experience', 'consultation_fee')
        }),
        ('System Information', {
            'fields': ('doctor_id', 'availability', 'status'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'patient', 'doctor', 'appointment_date', 'time_slot', 'purpose', 'status')
    list_filter = ('status', 'appointment_date', 'doctor__specialization')
    search_fields = ('appointment_id', 'patient__first_name', 'patient__last_name', 'doctor__first_name')
    date_hierarchy = 'appointment_date'
    ordering = ('-appointment_date', 'time_slot')
    
    def patient_name(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"
    
    def doctor_name(self, obj):
        return f"Dr. {obj.doctor.first_name} {obj.doctor.last_name}"