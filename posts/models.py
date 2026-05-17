from django.db import models
# CREATE TABLE IF NOT EXISTS ...
# class Model(models.Model): ...

# SELECT * FROM posts 

# modelname.objects.all()






# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    p = models.DateTimeField()

    def str(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.IntegerField()
    is_published = models.BooleanField(default=False)
    user = models.ImageField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    


    



