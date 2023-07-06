from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post_images',null=True,default='static/img/img-01.jpg')
