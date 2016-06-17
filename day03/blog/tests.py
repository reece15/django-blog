from django.test import TestCase
from blog.models import *
# Create your tests here.


class TestModel(TestCase):
	def setUp(self):
		user = Users.objects.create(name="123", password="111", email = "123@qq.com" )
		tag = Tags.objects.create(name='book')
		article = Article.objects.create(title='test', readCnt=1, user=user, tags=tag, content='test')

	def testRead(self):
		a = Article.objects.filter(readCnt=1)
		b = Tags.objects.filter(name='book')
		print b
		print a[0].tags