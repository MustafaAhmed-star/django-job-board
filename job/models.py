from tkinter import CASCADE
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE =( 
     ('Full Time','Full Time'),
     ('Part Time','Part Time'),
)

class Job(models.Model):

    owner = models.ForeignKey(User ,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15 ,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at =models.DateTimeField(auto_now=True) 
    vacancy =models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience =models.IntegerField(default=1)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , blank=True, null=True)
    image = models.ImageField(upload_to ='jobs/',null = True , blank = True)
    slug = models.SlugField(null=True ,blank=True )


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)    

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name =models.CharField(max_length=50)
    email =models.EmailField()
    website =models.URLField() 
    cv = models.FileField(upload_to='apply/')
    coverletter =models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name