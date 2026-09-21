import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from main.models import Experience, Skill, Project
from main.forms import ProjectForm
# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        "name": "Roisul Umam",
        "short_name": "Rois",
        "npm": "2506620210",
        "avatar_url": "/static/img/rois.jpg",
        "avatar_url_back": "/static/img/rois_2.jpg",
        "kicker": "Computer Science · Universitas Indonesia",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with a strong interest "
            "in data engineering — turning raw data into meaningful insights and "
            "understanding the systems behind large-scale data processing."
        ),
        "social_links": [
            {"name": "GitHub", "url": "https://github.com/Roisul-Umam", "display": "Roisul-Umam", "icon": "fa-brands fa-github"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/roisul-umam-83577b302/?locale=en", "display": "Roisul Umam", "icon": "fa-brands fa-linkedin"},
            {"name": "Email", "url": "mailto:umamr545@gmail.com", "display": "umamr545@gmail.com", "icon": "fa-solid fa-envelope"},
        ],
        "navigation_links": [
                    {"name": "Profile", "url_name": "main:show_main"},
                    {"name": "Experience", "url_name": "main:show_experience"},
                    {"name": "Projects", "url_name": "main:show_projects"},
                ],
        "last_login": last_login,
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Rois",
        "short_name": "Rois",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
 
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")
 
    context = {
        "name": "Rois",
        "short_name": "Rois",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {
        "name": "Rois",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {
        "name": "Rois",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response