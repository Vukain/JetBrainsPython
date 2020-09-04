from django.shortcuts import render
from django.views import View
from resume.models import Resume
# Create your views here.


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resumes.html', context={'users': resumes})
