from django.db import models

class Images(models.Model):
	sofa = models.ImageField(upload_to='', default = 'i1.jpg')
	curtain = models.ImageField(upload_to='', default = 'i1.jpg')
