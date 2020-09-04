"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from menu.views import MenuView, HomeView, MySignupView, MyLoginView, resume_new, vacancy_new
from resume.views import ResumesView
from vacancy.views import VacanciesView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuView.as_view()),
    path('home', HomeView.as_view()),
    path('resumes', ResumesView.as_view()),
    path('resume/new', resume_new, name='resume_new'),
    path('vacancies', VacanciesView.as_view()),
    path('vacancy/new', vacancy_new, name='vacancy_new'),
    path('login', MyLoginView.as_view()),
    path('signup', MySignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
]
