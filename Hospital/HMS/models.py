from datetime import datetime

from django.db import models
from django.http import request
from django.urls import reverse

# from user_registration.models import PatientUser, StaffUser

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Others'))


# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    location = models.TextField(blank=True, null=True, default="")

    def __str__(self):
        return self.department_name

    def get_absolute_url(self):
        return reverse('HMS:department_list')


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    dob = models.DateTimeField(blank=True)
    doj = models.DateTimeField(default=datetime.now())
    degree = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='in_doctor')
    specialist = models.CharField(max_length=100, default="None")
    surgeon = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.department}'

    def get_absolute_url(self):
        return reverse('HMS:doctor_list')


class Patient(models.Model):
    name = models.CharField(max_length=68)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    mobile = models.PositiveBigIntegerField(max_length=10, blank=True, null=True)
    doctor = models.ManyToManyField(Doctor, through='DoctorPatientRelation')
    dob = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        print('save function ')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('HMS:patient_list')

    def __str__(self):
        return f'{self.name} | {self.mobile}'


class DoctorPatientRelation(models.Model):
    doctor_to = models.ForeignKey(Doctor, verbose_name='Doctor', related_name='my_doctor', on_delete=models.CASCADE)
    patient_to = models.ForeignKey(Patient, verbose_name='Patient', related_name='my_patient', on_delete=models.CASCADE)
    medical_file = models.FileField(upload_to='medicalfile', default='medicalfile/test.txt')
    diagnosis = models.TextField(blank=True, null=True)
    date_last_visit = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.doctor_to.name} {self.patient_to.name}'

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        unique_together = ('doctor_to', 'patient_to')
