from django import forms
from .models import *


#
# class DepartmentForm(forms.Form):
#     class Meta:
#         fields = ('department_name', 'location')
#         ordering = 'department_name'
#
#
class DateInput(forms.DateInput):
    input_type = 'date'


class DoctorForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    doj = forms.DateField(widget=DateInput)

    class Meta:
        model = Doctor
        fields = ('name', 'degree', 'department', 'specialist', 'surgeon', 'doj', 'dob', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doj'].label = "Date of Joining"
        self.fields['dob'].label = "Date of Birth"


#
class PatientForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = Patient
        fields = ('name', 'gender', 'dob', 'email', 'mobile', 'doctor')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dob'].label = "Date of Birth"
