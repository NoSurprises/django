from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    author = models.ForeignKey(User, )
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    draft = models.BooleanField(default = True)
    slug = models.SlugField(null = True, blank = True)
    rating = models.IntegerField(default = 0)
    
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return '/blog/%s/' %(self.slug)
        


class Comment(models.Model):
    author = models.CharField(max_length = 100)
    body = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    
    def __unicode__(self):
        return (self.author + ' ---- commented on ----' + self.post.title)
        
    

