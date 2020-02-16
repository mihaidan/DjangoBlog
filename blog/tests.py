from django.test import TestCase

from .models import Post
from .forms import PostForm
from .views import create_post

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test Blog', description='test blog')
        Post.objects.create(title='Test Blog Too', description='test blog again')


    # checking if the two posts were created properly
    def test_posts_exist(self):
        post_one = Post.objects.get(slug='test-blog')
        post_two = Post.objects.get(slug='test-blog-too')

        self.assertEqual(post_one.title, 'Test Blog')
        self.assertEqual(post_two.description, 'test blog again')


    # checking if the PostForm works properly
    def test_PostForm(self):
        post_form = PostForm(data={'title': 'Some title', 'description': 'some description'})

        self.assertTrue(post_form.is_valid())


    # checking if the create_post view works as intended
    def test_create_post(self):
        context = {
            'title': 'I Like Blogs',
            'description': 'blogs are cool',
        }

        #(call the create_post view here)

        #post = Post.objects.get(slug='i-like-blogs')

        #self.assertEqual(post.title, 'I Like Blogs')


    # checking if the edit functionality works
    def test_edit_post(self):
        pass