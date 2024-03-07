from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def project_list(request):

    projects = Project.objects.all()

    return render(request, "content/project_list.html", {"projects": projects})



def project_new(request):
    form = ProjectForm()
    return render(request, "content/project_new.html", {"form": form})