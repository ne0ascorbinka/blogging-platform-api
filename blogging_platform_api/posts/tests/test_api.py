from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from posts.models import Category, Tag, Post

class APITests(APITestCase):
    def setUp(self):
        # Set up initial data
        self.category = Category.objects.create(name="Technology")
        self.tag1 = Tag.objects.create(name="Programming")
        self.tag2 = Tag.objects.create(name="Tech")
        self.post = Post.objects.create(
            title="Sample Post",
            content="This is a sample blog post.",
            category=self.category
        )
        self.post.tags.set([self.tag1, self.tag2])

        # Get URLs dynamically
        self.list_url = reverse('post-list')  # Name is auto-generated as '<basename>-list'
        self.detail_url = reverse('post-detail', kwargs={'pk': self.post.id})

    def test_post_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Sample Post")

    def test_post_creation(self):
        data = {
            "title": "New Post",
            "content": "This is a new blog post.",
            "category": "Technology",
            "tags": ["Tech", "Programming"]
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_post_filter_by_term(self):
        response = self.client.get(f'{self.list_url}?term=Tech')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Sample Post")

    def test_post_retrieve(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Sample Post")
