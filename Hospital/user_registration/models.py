from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
JOB_SPECIFICATION = (('1', 'Doctor'), ('2', 'Nurse'), ('3', 'Lab Staff'), ('5', 'Cleaning Staff'), ('6', 'Other'))


class PatientUser(models.Model):
    reg_user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.reg_user}'



class StaffUser(models.Model):
    reg_user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=1, choices=JOB_SPECIFICATION)

    def __str__(self):
        return f'{self.reg_user}'