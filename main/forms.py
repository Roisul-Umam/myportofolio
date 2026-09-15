import re
from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tags",
            "link",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tags": "Tag Proyek",
            "link": "URL Proyek",
            "project_image_url": "Gambar Proyek (link Google Drive atau link gambar langsung)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Project Name",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Project Description",
                    "rows": 3,
                }
            ),
            "tags": TextInput(
                attrs={
                    "placeholder": "Project Tags (separate with commas, e.g., Django, Python, CSS)",
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "Project Link (e.g., https://github.com/Burhan/burhanquestv4)",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "Paste Google Drive link",
                }
            ),
        }

    def clean_project_image_url(self):
        url = self.cleaned_data.get("project_image_url")

        if not url:
            return url

        patterns = [
            r"drive\.google\.com/file/d/([a-zA-Z0-9_-]+)",
            r"drive\.google\.com/open\?id=([a-zA-Z0-9_-]+)",
            r"drive\.google\.com/uc\?id=([a-zA-Z0-9_-]+)",
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                file_id = match.group(1)
                return f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"

        return url