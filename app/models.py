import email
from email.policy import default
# from tkinter import N
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50, default="", blank=True, null=True)

    def __str__(self):
        return str(self.name)



# class Tag(models.Model):
#     tag_name = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.tag_name)



class Blog(models.Model):
    user_name=models.ForeignKey('user.CustomUser',on_delete=models.CASCADE, default=None)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    title=models.CharField(max_length=100, default="")
    thought=models.CharField(max_length=100, default="")

    desc=HTMLField()
    desc1=HTMLField(default="")

    date=models.DateTimeField(auto_now_add=True, null=True)
    liked=models.ManyToManyField('user.CustomUser', default=None, blank=True, related_name='liked')

    # tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    image = models.ImageField( upload_to='image/', default="")
    image1 = models.ImageField( upload_to='image/', default="")

    
    
    def __str__(self):
        return str(self.id)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
    # def get_absolute_url(self):
    #     return reverse('blog',kwargs={'pk':self.pk})
    

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, default=True, related_name='blog')
    value=models.CharField(choices=LIKE_CHOICES,max_length=50,default='Like')
    
    def __str__(self):
        return str(self.blog)
    
    
class Comment(models.Model):
        
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True)
    content = models.TextField()
    email=models.EmailField( max_length=254, default="" , null=True)
    website = models.CharField( max_length=50, default="" , null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name="comments", blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.id)


class Contact(models.Model):
        
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, blank=True, default=True)
    content = models.TextField()
    email=models.EmailField( max_length=254, default="" , null=True)
    website = models.CharField( max_length=50, default="" , null=True)
   
    
    def __str__(self):
        return str(self.id)