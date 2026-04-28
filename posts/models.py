from django.db import models

# CREATE TABLE IF NOT EXISTS ...
# class Model(models.Model): ...

# SELECT * FROM posts 

# modelname.objects.all()






# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    user = models.ImageField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    p = models.DateTimeField()

    def str(self):
        return self.title
    



