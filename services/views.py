from django.shortcuts import render
from .models import Project

# Create your views here.
def services(request):
    projects = Project.objects.all()
    return render(request, 'services/services.html', {'projects' :projects})