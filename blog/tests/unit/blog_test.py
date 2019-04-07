from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test title', 'Test author')

        self.assertEqual('Test title', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test by Test author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test author')
        b2 = Blog('My Day', 'Rolf')
        b.posts = ['test']
        b2.posts = ['test', 'another test']

        self.assertEqual(b.__repr__(), 'Test by Test author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')

