from django.db import models
# from autoslug import AutoSlugField

# Create your models here.
class Hero(models.Model):
    images          =   models.ImageField(upload_to='hero-image/', null=True, blank=True,)
    discription         =   models.TextField(blank=True,null=True)
    text                =   models.CharField(blank=True,null=True ,max_length=300)
    is_active           =   models.BooleanField(default=True)

class Slider(models.Model):
   image= models.ImageField(upload_to='slider-image/', null=True, blank=True,)
   subtitle=models.CharField(max_length=200)
   header1=models.CharField(max_length=300)
   header2=models.CharField(max_length=300)
   date  =  models.DateTimeField(auto_now_add=False , null=True, blank=True)
   is_active = models.BooleanField(default=True)
