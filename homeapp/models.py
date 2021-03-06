from django.db import models
from PIL import Image

# Create your models here.
class Intro(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images')
    name = models.CharField(max_length=50)
    title = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Resume(models.Model):
    a1 = models.TextField()
    a2 = models.TextField()
    a3 = models.TextField()
    a4 = models.FileField(default='resume.pdf', upload_to='pdf')
    
class MySkill(models.Model):    
    s1 = models.CharField(max_length=50)
    s2 = models.CharField(max_length=50)
    s3 = models.CharField(max_length=50)
    s4 = models.CharField(max_length=50)
    s5 = models.CharField(max_length=50)
    s6 = models.CharField(max_length=50)
    s7 = models.CharField(max_length=50)

class MyProject(models.Model):
    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    p4 = models.TextField()