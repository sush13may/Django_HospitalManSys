from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import operator

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView, RedirectView, DetailView
from django.views.generic.edit import ModelFormMixin

from HMS.forms import PatientForm, DoctorForm
from HMS.models import Department, Doctor, Patient, DoctorPatientRelation

# pip install django-braces
from braces.views import SelectRelatedMixin, PrefetchRelatedMixin


def index(request):
    return HttpResponse("Welcome HMS")


class DepartmentCreate(LoginRequiredMixin, CreateView):
    fields = ('department_name', 'location')
    model = Department


class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm


class PatientCreate(LoginRequiredMixin, CreateView):
    # fields = ('name', 'gender', 'email', 'mobile', 'dob')
    form_class = PatientForm
    model = Patient

    def get_success_url(self):
        print('get_succeess')
        if self.request.POST.get('save_add'):
            print('save_add')
            messages.success(self.request, "Patient records are saved.")
            return reverse("HMS:create_patient")
        elif self.request.POST.get('save'):
            print('save88888888888888')
            return reverse("HMS:patient_list")


class DoctorPatientRelationCreate(LoginRequiredMixin, CreateView, ModelFormMixin):
    model = DoctorPatientRelation
    fields = ('patient_to', 'doctor_to', 'diagnosis', 'medical_file')


class DepartmentList(LoginRequiredMixin, ListView):
    model = Department
    fields = '__all__'


class DoctorList(LoginRequiredMixin, ListView):
    model = Doctor
    fields = '__all__'


class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    # prefetch_related = ('doctor',)
    fields = ('name', 'gender', 'dob', 'email', 'mobile')
    # fields = '__all__'

    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['doctor_list'] = Doctor.objects.filter()


class PatientDetail(DetailView, LoginRequiredMixin, ModelFormMixin, PrefetchRelatedMixin):
    model = Patient
    prefetch_related = ('doctor',)
    form_class = PatientForm


class PatientUpdateView(UpdateView, LoginRequiredMixin, PrefetchRelatedMixin):
    model = Patient

    # def get_redirect_url(self):
    #     return reverse('HMS:patient_list')
    # def post(self, request, *args, **kwargs):

    # patient = get_object_or_404(Patient, id=self.kwargs.get('id'))
    #
    # if patient is not None:


def doctorsearch(request):
    print("**********")
    if request.method == "GET":

        name = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if name is not None:
            # lookup = Q(name__icontain == name) | Q(department__icontain == name) | Q(email__icontain == name) | Q(
            #     specialist__icontain == name)
            results = Doctor.objects.filter(Q(name__icontains=name) |
                                            Q(email__icontains=name) |
                                            Q(specialist__icontains=name) |
                                            Q(department__department_name__icontains=name) |
                                            Q(department__location__icontains=name)).distinct()

            context = {'object_list': results, 'submitbutton': submitbutton}
            return render(request, 'HMS/doctor_list.html', context)
        else:
            return render(request, 'HMS/doctor_list.html')
    else:
        return render(request, 'HMS/doctor_list.html')


def departmentsearch(request):
    print("**********")
    if request.method == "GET":

        name = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if name is not None:
            results = Department.objects.filter(Q(department_name__icontains=name) |
                                                Q(location__icontains=name))
            print(results)
            context = {'object_list': results, 'submitbutton': submitbutton}
            return render(request, 'HMS/department_list.html', context)
        else:
            return render(request, 'HMS/department_list.html')
    else:
        return render(request, 'HMS/department_list.html')


def patientsearch(request):
    if request.method == 'GET':
        name = request.GET.get('q')
        submitbutton = request.GET.get('submit')

        if name is not None:
            lookup = (Q(name__icontains=name) | Q(email__icontains=name) |
                      Q(dob__icontains=name) | Q(dob__icontains=name) |
                      Q(mobile__icontains=name) | Q(my_doctor__name__icontains=name))
            results = Patient.objects.filter(lookup).distinct()

            # if len(results) < 1:
            #     try:
            #         results = Patient.objects.filter(my_doctor__icontains=name)
            #     except:
            #         messages.error(request,"Something Went wrong")

            context = {'object_list': results, 'submitbutton': submitbutton}
            return render(request, 'HMS/patient_list.html', context)
        else:
            return render(request, 'HMS/patient_list.html')
    else:
        return render(request, 'HMS/patient_list.html')
