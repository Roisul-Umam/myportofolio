import uuid
from datetime import timedelta

from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience

PASSWORD = "test-password-123"


class ExperienceAPITestBase(APITestCase):
    """Empat peran: pengunjung (anonim), pengguna biasa, Editor, dan pemilik (superuser)."""

    def setUp(self):
        editor_group = Group.objects.create(name="Editor")  # database uji selalu kosong
        self.regular = User.objects.create_user("biasa", email="biasa@example.com", password=PASSWORD)
        self.editor = User.objects.create_user("editor", email="editor@example.com", password=PASSWORD)
        self.editor.groups.add(editor_group)
        self.owner = User.objects.create_superuser("pemilik", email="pemilik@example.com", password=PASSWORD)

        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Magang Data Engineer",
            "description": "Membangun data pipeline.",
            "category": "internship",
        }

    def assertExperienceUnchanged(self):
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertEqual(Experience.objects.count(), 1)


class ExperienceReadAPITest(ExperienceAPITestBase):
    def test_visitor_can_list_and_see_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Asisten Dosen PBP")
        self.assertEqual(response.data[0]["category_display"], "Part-Time")
        self.assertTrue(response.data[0]["is_ongoing"])

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(self.experience.id))

    def test_completed_experience_is_not_ongoing(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(self.detail_url)
        self.assertFalse(response.data["is_ongoing"])

    def test_search_uses_title_query_param(self):
        Experience.objects.create(title="Juara Kompetisi Data", description="Lomba", category="competition")
        response = self.client.get(self.list_url, {"title": "kompetisi"})
        self.assertEqual([e["title"] for e in response.data], ["Juara Kompetisi Data"])
        self.assertEqual(self.client.get(self.list_url, {"title": "tidak-ada"}).data, [])

    def test_missing_experience_returns_404(self):
        url = reverse("api:experience-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_sensitive_account_data_is_not_exposed(self):
        self.experience.starred_by.add(self.regular)
        response = self.client.get(self.list_url)
        body = response.content.decode()
        self.assertEqual(response.data[0]["starred_by_names"], "biasa")  # username boleh
        self.assertNotIn("biasa@example.com", body)
        self.assertNotIn("password", body)
        self.assertNotIn("pbkdf2", body)

    def test_browsable_api_can_be_opened(self):
        response = self.client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ExperienceWritePermissionAPITest(ExperienceAPITestBase):
    def assertAllWritesForbidden(self):
        responses = [
            self.client.post(self.list_url, self.payload, format="json"),
            self.client.put(self.detail_url, self.payload, format="json"),
            self.client.patch(self.detail_url, {"title": "Diretas"}, format="json"),
            self.client.delete(self.detail_url),
        ]
        for response in responses:
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertExperienceUnchanged()  # cek isi database, bukan hanya status

    def test_visitor_cannot_write(self):
        self.assertAllWritesForbidden()

    def test_regular_user_cannot_write(self):
        self.client.force_authenticate(self.regular)
        self.assertAllWritesForbidden()

    def test_editor_can_patch_and_put(self):
        self.client.force_authenticate(self.editor)
        response = self.client.patch(self.detail_url, {"title": "Judul Baru"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Judul Baru")
        self.assertEqual(self.experience.category, "part-time")  # PATCH tidak menyentuh field lain

        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Magang Data Engineer")
        self.assertEqual(self.experience.category, "internship")

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(self.editor)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Experience.objects.filter(title="Magang Data Engineer").exists())

        response = self.client.patch(self.detail_url, {"category": "research"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.category, "research")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_delete_missing_experience_returns_404(self):
        self.client.force_authenticate(self.owner)
        url = reverse("api:experience-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.delete(url).status_code, status.HTTP_404_NOT_FOUND)


class ExperienceValidationAPITest(ExperienceAPITestBase):
    def setUp(self):
        super().setUp()
        self.client.force_authenticate(self.owner)

    def test_missing_required_fields_returns_400(self):
        response = self.client.post(self.list_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertIn("description", response.data)
        self.assertEqual(Experience.objects.count(), 1)

    def test_text_with_only_html_tags_is_rejected(self):
        for field in ("title", "description"):
            response = self.client.post(
                self.list_url, {**self.payload, field: "<script></script>"}, format="json",
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Experience.objects.count(), 1)

    def test_html_tags_are_stripped(self):
        payload = {
            **self.payload,
            "title": "  <b>Magang</b> Bersih  ",
            "description": "<script>alert(1)</script>Deskripsi aman",
        }
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        experience = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(experience.title, "Magang Bersih")
        self.assertNotIn("<", experience.description)
        self.assertIn("Deskripsi aman", experience.description)

    def test_invalid_category_and_thumbnail_are_rejected(self):
        response = self.client.post(self.list_url, {**self.payload, "category": "bukan-kategori"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("category", response.data)

        response = self.client.post(self.list_url, {**self.payload, "thumbnail": "javascript:alert(1)"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("thumbnail", response.data)
        self.assertEqual(Experience.objects.count(), 1)

    def test_google_drive_thumbnail_is_converted(self):
        payload = {**self.payload, "thumbnail": "https://drive.google.com/file/d/abc123/view?usp=sharing"}
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["thumbnail"], "https://drive.google.com/thumbnail?id=abc123&sz=w1000")

    def test_ended_at_before_started_at_is_rejected(self):
        past = (self.experience.started_at - timedelta(days=1)).isoformat()
        response = self.client.patch(self.detail_url, {"ended_at": past}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("ended_at", response.data)
        self.experience.refresh_from_db()
        self.assertIsNone(self.experience.ended_at)

    def test_put_without_required_fields_returns_400(self):
        response = self.client.put(self.detail_url, {"title": "Saja"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertExperienceUnchanged()

    def test_patch_with_blank_title_returns_400(self):
        response = self.client.patch(self.detail_url, {"title": "<b></b>"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertExperienceUnchanged()

    def test_computed_fields_are_read_only(self):
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True, "is_ongoing": False,
            "starred_by_names": "palsu", "starred_by": [self.regular.pk],
            "started_at": "2000-01-01T00:00:00Z",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertTrue(response.data["is_ongoing"])
        experience = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(experience.starred_by.count(), 0)
        self.assertGreater(experience.started_at.year, 2000)


class ExperienceStarAPITest(ExperienceAPITestBase):
    def test_visitor_cannot_star(self):
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_user_can_star_and_unstar(self):
        self.client.force_authenticate(self.regular)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["star_count"], 1)
        self.assertTrue(response.data["is_starred"])
        self.assertIn(self.regular, self.experience.starred_by.all())

        response = self.client.post(self.star_url)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_is_starred_is_per_user(self):
        self.experience.starred_by.add(self.regular)
        self.client.force_authenticate(self.editor)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.data["star_count"], 1)
        self.assertFalse(response.data["is_starred"])

    def test_star_uses_request_user_not_body(self):
        self.client.force_authenticate(self.regular)
        response = self.client.post(
            self.star_url, {"user": self.owner.pk, "starred_by": [self.owner.pk]}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(self.experience.starred_by.all()), [self.regular])

    def test_star_on_missing_experience_returns_404(self):
        self.client.force_authenticate(self.regular)
        url = reverse("api:experience-star", args=[uuid.uuid4()])
        self.assertEqual(self.client.post(url).status_code, status.HTTP_404_NOT_FOUND)


class ExperienceCSRFAPITest(ExperienceAPITestBase):
    """force_authenticate melewati CSRF, jadi di sini memakai .login() + enforce_csrf_checks."""

    def login_client(self, username):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username=username, password=PASSWORD))
        return client

    def test_write_without_csrf_token_is_rejected(self):
        client = self.login_client("pemilik")
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("CSRF", str(response.data["detail"]))
        self.assertEqual(Experience.objects.count(), 1)

        response = client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_patch_and_star_without_csrf_token_are_rejected(self):
        editor_client = self.login_client("editor")
        response = editor_client.patch(self.detail_url, {"title": "Diretas"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertExperienceUnchanged()

        regular_client = self.login_client("biasa")
        self.assertEqual(regular_client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_experience_page_sets_csrf_cookie_for_regular_user(self):
        client = APIClient()
        client.login(username="biasa", password=PASSWORD)
        response = client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("csrftoken", response.cookies)

    def test_write_with_csrf_token_is_accepted(self):
        client = self.login_client("pemilik")
        page = client.get(reverse("main:show_experience"))
        token = page.cookies["csrftoken"].value
        response = client.post(self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Experience.objects.count(), 2)