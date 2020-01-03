from django.test import TestCase
from django.conf import settings
from .models import Post, Comment
from django.contrib.auth.models import User

# Create your tests here.

class BlogTests(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_post_with_comments(self):
        user = User.objects.create_user(username='testuser111', password='12345')
        p = Post(title="I'm here", text='aaaaaaaabbbbbb', author=user)
        p.save()
        count_before = p.comments.count()
        c = Comment(author='dima', text='i like pooping')
        c.post = p
        c.save()
        count_after = p.comments.count()
        self.assertIs(count_after-count_before, 1)


