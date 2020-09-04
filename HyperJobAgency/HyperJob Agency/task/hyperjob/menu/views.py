from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import ResumeForm, VacancyForm
from resume.models import Resume
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden


# Create your views here.
def vacancy_new(request):

    if request.user.is_staff:
        if request.method == "POST":
            form = VacancyForm(request.POST)

            if form.is_valid():
                resume = Vacancy.objects.create(author=request.user, description=request.POST.get('description'))
                return redirect('/home')
        return redirect("/home")
    return HttpResponseForbidden()


def resume_new(request):

    if request.user.is_authenticated and not request.user.is_staff:
        if request.method == "POST":
            form = ResumeForm(request.POST)

            if form.is_valid():
                resume = Resume.objects.create(author=request.user, description=request.POST.get('description'))
                return redirect('/home')
        return redirect("/home")
    return HttpResponseForbidden()




class MenuView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'menu.html', context=None)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        resume = ResumeForm()
        vacancy = VacancyForm()
        return render(request, 'home.html', context={'resume': resume, 'vacancy': vacancy})


class MySignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'