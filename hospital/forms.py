from django import forms
from django.core.validators import validate_email

from .models import Department, Doctor, Appointment

# class AppointmentForm(forms.Form):
#     department_id = forms.ChoiceField(choices=Department.objects.values_list('id', 'title'))
#     doctor_id = forms.ChoiceField(choices=Doctor.objects.values_list('id', 'first_name'))
#     patient_name = forms.CharField(max_length=255)
#     patient_email = forms.EmailField(validators=[validate_email])
#     appointment_date = forms.DateField()

# def clean(self):
#     cleaned_data = super().clean()
#     # Custom validation and cleaning logic goes here
#     return cleaned_data
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
