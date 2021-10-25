from django.db import models

# Create your models here.

class Demo_Post(models.Model):
    text= models.TextField()
    template_name ='post.html'

    def __str__(self):
        return self.text[:50]