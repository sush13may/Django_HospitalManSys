from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from . import forms


# Create your views here.
def test(request):
    return HttpResponse("you are registered here successfully")


def patient_register(request, type):
    print(type)
    if type =='S':
        form_class = forms.StaffUserForm()
    elif type =='P':
        form_class = forms.PatientUserForm()

    main_form = forms.UserForm()
    if request.method == "POST":
        if type == 'S':
            print('77777')
            form_class = forms.StaffUserForm(request.POST)
        elif type == 'P':
            form_class = forms.PatientUserForm(request.POST)
        main_form = forms.UserForm(request.POST)
        if form_class.is_valid() and main_form.is_valid():
            print('***************'+type)
            obj = main_form.save()
            obj1 = form_class.save(commit=False)
            obj1.reg_user = obj
            obj1.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(f"Something is wrong with form{form_class.is_valid()}, {main_form.is_valid()}")

    return render(request, 'user_registration/registration.html', {'form': form_class, 'main_form': main_form})


# class StaffRegister(CreateView):
#     form_class = forms.StaffUserForm
#     main_form = forms.UserForm
#     template_name = "user_registration/registration.html"
#     success_url = reverse_lazy('user_registration:test')
