from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        respone = self.client.get("/")
        self.assertEqual(respone.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")


class AboutPageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
