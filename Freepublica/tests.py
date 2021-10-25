from django.core.checks.messages import DEBUG
from django.test import TestCase

from django.urls import reverse

from .models import*
# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        Demo_Post.objects.create(text='just test')


    def test_text_content(self):
        post=Demo_Post.objects.get(id=1)
        object_list=f'{post.text}'
        self.assertEqual(object_list,'just test')



class HomepageView(TestCase):

    def setUp(self):
        Demo_Post.objects.create(text='this is test 2')


    def test_if_resp_is_true(self):
        resp= self.client.get('')
        self.assertEqual(resp.status_code,200)

    
    def test_if_urlis_working(self):
        resp=self.client.get(reverse('index'))
        self.assertEqual(resp.status_code,200)
    

    def test_for_correct_template(self):
        resp=self.client.get(reverse('index'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed('index.html')








