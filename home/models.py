from django.db import models

# Create your models here.
class place(models.Model):
    type=models.TextField()
    img=models.ImageField(upload_to='pics')
    
class customer(models.Model):
    name=models.TextField(max_length=50)
    desc=models.TextField(max_length=100)
    pic=models.ImageField(upload_to='pics')    

class movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()


