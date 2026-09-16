import uuid
from django.db import models

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
        ('competition', 'Competition'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="Contoh: devicon-python-plain (lihat devicon.dev)",
    )
    icon_url = models.URLField(
        blank=True,
        help_text="Link gambar sendiri (opsional). Kalau diisi, ini dipakai duluan, mengalahkan icon_class.",
    )
    capabilities = models.TextField(
        blank=True,
        help_text="Satu poin per baris, contoh:\nBasic Python\nBasic Pandas",
    )

    def __str__(self):
        return self.name

    @property
    def capabilities_list(self):
        return [c.strip() for c in self.capabilities.splitlines() if c.strip()]


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=200) 
    link = models.URLField(blank=True, null=True)
    project_image_url = models.URLField(blank=True, null=True)

    @property
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]