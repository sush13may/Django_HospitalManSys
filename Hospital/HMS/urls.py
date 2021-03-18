from django.urls import path

from HMS import views

app_name = 'HMS'
urlpatterns = [
    path('', views.index, name='index'),
    path('patient', views.PatientCreate.as_view(), name='create_patient'),
    path('doctor', views.DoctorCreate.as_view(), name='create_doctor'),
    path('department', views.DepartmentCreate.as_view(), name='create_department'),
    path('patient_medical_update/',views.DoctorPatientRelationCreate.as_view(), name='create_doctorpatientrelation'),
    path('department/list/',views.DepartmentList.as_view(), name='department_list'),
    path('doctor/list/',views.DoctorList.as_view(), name='doctor_list'),
    path('patient/list/',views.PatientList.as_view(), name='patient_list'),
    path('doctor/search/', views.doctorsearch, name='doctor_search'),
    path('department/search/', views.departmentsearch, name='department_search'),
    path('Patient/search/', views.patientsearch, name='patient_search'),
    path('patient/edit/<int:pk>', views.PatientDetail.as_view(), name='edit_patient'),
    path('patient/update/<int:pk>', views.PatientUpdateView.as_view(), name="patient_update"),

]
