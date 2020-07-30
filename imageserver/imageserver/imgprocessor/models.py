from django.db import models

# Create your models here.
class TextImageResponse(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=128, blank=True, default='Empty Title')
    content = models.TextField(max_length=512, blank=True, default='Empty Content')
    imageUrl = models.ImageField()

    class Meta:
        ordering = ['createdAt']


class ClientImageRequest(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=128, blank=True, default='Empty Title')
    content = models.TextField(max_length=512, blank=True, default='Empty Content')
    

    class Meta: 
        ordering = ['createdAt']

class NameFields(models.Model):
    name = models.CharField(max_length=48)

    class Meta:
        ordering = ['name']