from django.urls import path
from . import views

app_name = 'user_registration'
urlpatterns = [

    path('register/<str:type>', views.patient_register, name='register'),
    path('test/', views.test, name='test')
]