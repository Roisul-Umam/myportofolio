from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill, Project
# Create your tests here.

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("api:experience-list")).json()
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category_display"], "Part-Time")
        self.assertTrue(data[0]["is_ongoing"])

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        data = self.client.get(reverse("api:experience-list")).json()

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(data[0]["is_ongoing"])
        
class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('main:show_projects')  

    def test_projects_url_and_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')  

    def test_projects_view_with_data(self):
        project = Project.objects.create(
            title="Portfolio Website",
            description="Website portofolio dengan Django",
            tags="Django, Python",
            link="https://github.com/example/portfolio"
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

        api_response = self.client.get(
            reverse('api:project-list')
        )

        self.assertEqual(api_response.status_code, 200)

        data = api_response.json()

        self.assertEqual(data[0]["title"], project.title)
        self.assertEqual(data[0]["description"], project.description)

    def test_projects_view_empty_state(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects found.")