from rest_framework.test import APITestCase
from posts.serializers import PostSerializer
from posts.models import Category, Tag, Post

class SerializerTests(APITestCase):
    def test_serializer_input_output(self):
        category = Category.objects.create(name="Technology")
        tag1 = Tag.objects.create(name="Programming")
        tag2 = Tag.objects.create(name="Tech")

        post = Post.objects.create(
            title="Sample Post",
            content="This is a sample blog post.",
            category=category
        )
        post.tags.set([tag1, tag2])

        # Serialize the post
        serializer = PostSerializer(post)
        self.assertEqual(serializer.data['title'], "Sample Post")
        self.assertEqual(serializer.data['category'], "Technology")
        self.assertIn("Programming", serializer.data['tags'])
        self.assertIn("Tech", serializer.data['tags'])

    def test_serializer_validation(self):
        # Test serializer with input data
        data = {
            "title": "New Post",
            "content": "Content for new post.",
            "category": "Technology",
            "tags": ["Tech", "Programming"]
        }
        serializer = PostSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        # Test output after saving
        serializer.save()
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, "New Post")
        self.assertEqual(post.category.name, "Technology")
