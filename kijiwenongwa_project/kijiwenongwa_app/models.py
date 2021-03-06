from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null= True,blank=True)
    facebook_url = models.CharField(max_length=255,null= True,blank=True)
    instagram_url = models.CharField(max_length=255,null= True,blank=True)
    twitter_url = models.CharField(max_length=255,null= True,blank=True)
    pinterest_url = models.CharField(max_length=255,null= True,blank=True)
    Email = models.EmailField(max_length=255,null= True,blank=True)
    Phone_number = models.CharField(max_length=13,null=True,blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    tittle = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    tittle_tag = models.CharField(max_length=50, default='kijiwenongwa')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    Category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.tittle + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('detail', args=str(self.id))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.tittle, self.name)
