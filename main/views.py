from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from main.models import Experience, Skill, Project
from main.forms import ProjectForm
# Create your views here.
def show_main(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        "name": "Roisul Umam",
        "short_name": "Rois",
        "npm": "2506620210",
        "avatar_url": "/static/img/rois.jpg",
        "kicker": "Computer Science · Universitas Indonesia",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with a strong interest "
            "in data engineering — turning raw data into meaningful insights and "
            "understanding the systems behind large-scale data processing."
        ),
        "social_links": [
            {"name": "GitHub", "url": "https://github.com/Roisul-Umam"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/roisul-umam-83577b302/?locale=en"},
            {"name": "Email", "url": "mailto:umamr545@gmail.com"}
        ],
        "navigation_links": [
                    {"name": "Profile", "url_name": "main:show_main"},
                    {"name": "Experience", "url_name": "main:show_experience"},
                    {"name": "Projects", "url_name": "main:show_projects"},
                ],
        "skills": skills,
        "projects": projects,
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Rois",
        "short_name": "Rois",
        "experience_list": Experience.objects.all(),
        "navigation_links": [
                    {"name": "Profile", "url_name": "main:show_main"},
                    {"name": "Experience", "url_name": "main:show_experience"},
                    {"name": "Projects", "url_name": "main:show_projects"},
                ],
    }
    return render(request, "experience.html", context)

def show_projects(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json", 
        json_response.content.decode("utf-8")
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Rois",  
        "short_name": "Rois",
        "project_list": projects,
        "navigation_links": [
                    {"name": "Profile", "url_name": "main:show_main"},
                    {"name": "Experience", "url_name": "main:show_experience"},
                    {"name": "Projects", "url_name": "main:show_projects"},
                ],
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Rois",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")