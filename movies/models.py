# Create your models here.
from django.db import models
# from autoslug import AutoSlugField
import uuid
import os
import random
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Count

# Create your models here.
class Category(models.Model):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name            =   models.CharField(max_length=255,db_index=True)
    image          =   models.ImageField(upload_to='category-image', null=True, blank=True,)
    # slug             =   AutoSlugField(populate_from='name',max_length=255,unique=True,null=True)
    description      =   models.TextField(blank=True,null=True)
    parent_id        =   models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, related_name='category_parent')
    is_active        =   models.BooleanField(default=True)   
    created_date     =   models.DateTimeField(auto_now_add=True)
    modified_date    =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})



class Movie(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name= 'product_categotry',null=True,blank=True) #many to one relation with Category
    title = models.CharField(max_length=150)
    minutes = models.PositiveIntegerField(default=0)
    seconds = models.PositiveIntegerField(default=0)
    director = models.CharField(max_length=150)
    stars = models.CharField(max_length=150)
    writers = models.CharField(max_length=150)
    description = models.CharField(max_length=450)
    detailed_description = models.TextField(blank=True)
    image=models.ImageField(upload_to='images/',null=False)
    website_url = models.URLField()
    releas_date = models.DateTimeField(auto_created=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Review.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Review.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Images(models.Model):
    product=models.ForeignKey(Movie,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
class Reviews(models.Model):
    
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    comment = models.TextField()
    rate = models.PositiveIntegerField()
    status=models.CharField(max_length=10,choices=STATUS, default=STATUS[0][0])
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
   



