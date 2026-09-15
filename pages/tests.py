from django.test import SimpleTestCase

# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_correct_pos(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)

class AboutPageTests(SimpleTestCase):
    def test_url_correct_pos(self):
        responce = self.client.get("/about/")
        self.assertEqual(responce.status_code, 200)