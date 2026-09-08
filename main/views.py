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
        "skills": skills,
        "projects": projects,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Rois",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    projects = Project.objects.all()  # sesuaikan sama model kamu
    context = {
        "name": "Rois",  # atau variabel yang sudah kamu pakai
        "projects": projects,
    }
    return render(request, "projects.html", context)