from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test author', 'Test title')

        self.assertEqual('Test title', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)