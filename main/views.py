import datetime
import json
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from main.models import Experience, Skill, Project
from main.forms import ProjectForm
from django.views.decorators.http import require_POST
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
            "CS student at Universitas Indonesia on a mission to become a "
            "Data Engineer. I love turning messy, chaotic data into clean, "
            "useful insights. Most of my time goes into building reliable data pipelines, "
            "playing with distributed databases, and making sure backend systems run smoothly and scale well."
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
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Rois",
        "short_name": "Rois",
        "title_query": title_query,
        "form": ProjectForm(),
        "can_manage": request.user.is_superuser,
        "can_edit": request.user.is_superuser or user_is_editor(request.user),
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project created successfully!")
        return redirect("main:show_projects")

    context = {
        "name": "Rois",
        "short_name": "Rois",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only superusers can create projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project created successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (request.user.is_superuser or user_is_editor(request.user)):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
 
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project successfully updated!")
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
    projects = Project.objects.all().prefetch_related("starred_by")
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    projects = list(projects)

    data = json.loads(serializers.serialize("json", projects))
    for item, project in zip(data, projects):
        starred = list(project.starred_by.all())
        item["fields"]["star_count"] = len(starred)
        item["fields"]["starred_by_names"] = ", ".join(u.username for u in starred)
        item["fields"]["is_starred"] = request.user in starred
        item["fields"].pop("starred_by", None)
    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please login.")
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

def user_is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response