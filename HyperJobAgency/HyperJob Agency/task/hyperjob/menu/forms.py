from django import forms
from resume.models import Resume
from vacancy.models import Vacancy


class ResumeForm(forms.Form):

    description = forms.CharField(max_length=1024)


class VacancyForm(forms.Form):

    description = forms.CharField(max_length=1024)