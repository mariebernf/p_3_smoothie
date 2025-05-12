from django.test import TestCase
from django.contrib.auth.models import User
from .models import Smoothie
from django.urls import reverse

# Tests 

class SmoothieTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.smoothie = Smoothie.objects.create(
            title='Berry Blast',
            description='A tasty berry smoothie.',
            ingredients='Berries, banana, milk',
            author=self.user
        )

    def test_smoothie_creation(self):
        self.assertEqual(self.smoothie.title, 'Berry Blast')
        self.assertEqual(self.smoothie.author.username, 'testuser')

    def test_smoothie_list_view(self):
        response = self.client.get(reverse('smoothie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Berry Blast')
