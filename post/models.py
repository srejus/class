from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='post',null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
