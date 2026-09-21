from django.urls import path

from main import views
from main.views import (
    delete_project,
    edit_project,
    get_projects_json,
    show_main,
    show_experience,
    create_project,
    register,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('projects/', views.show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<int:project_id>/edit/", edit_project, name="edit_project"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]