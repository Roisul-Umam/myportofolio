from django.shortcuts import render
from main.models import Experience, Skill, Project
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
    projects = Project.objects.all()  
    context = {
        "name": "Rois",  
        "short_name": "Rois",
        "projects": projects,
        "navigation_links": [
                    {"name": "Profile", "url_name": "main:show_main"},
                    {"name": "Experience", "url_name": "main:show_experience"},
                    {"name": "Projects", "url_name": "main:show_projects"},
                ],
    }
    return render(request, "projects.html", context)