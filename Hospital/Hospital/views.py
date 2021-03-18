from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


class TestPageView(TemplateView):
    template_name = 'registertype.html'


class HomePageView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


def login_request(request):
    message = ""

    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print("*********************************")
            if user.is_active:
                print('######################################')
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                message = 'User is disabled'
        else:
            message = 'Username and Password is not matching'

    return render(request, 'login.html', {'message': message})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
