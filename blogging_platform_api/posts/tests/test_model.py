from django.test import TestCase
from posts.models import Category, Tag, Post

class TestModel(TestCase):
    def test_category_creation(self):
        category, created = Category.objects.get_or_create(name="Technology")
        self.assertTrue(created)
        self.assertEqual(category.name, "Technology")

    def test_tag_creation(self):
        tag, created = Tag.objects.get_or_create(name="Programming")
        self.assertTrue(created)
        self.assertEqual(tag.name, "Programming")

    def test_post_creation(self):
        category = Category.objects.create(name="Technology")
        post = Post.objects.create(
            title="Sample Post",
            content="This is a sample blog post.",
            category=category
        )
        post.tags.add(Tag.objects.create(name="Tech"))
        self.assertEqual(post.title, "Sample Post")
        self.assertEqual(post.category.name, "Technology")
        self.assertEqual(post.tags.first().name, "Tech")
