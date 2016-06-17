from django.db import models
from blog.models import Tags

def loadTags(req):
	tags = Tags.objects.all()
	return {'tags':tags}