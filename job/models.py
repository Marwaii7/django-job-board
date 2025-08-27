from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

Joptype=(
  ('part time' , 'part time'),
  ('Full time' , 'Full time'),
)

def image_upload( instance,filename):
  imagename,extension = filename.split(".")
  return " jobs/%s/%s.%s" %(instance.id,instance.id,extension)

# Create your models here.
class Job (models.Model):
  Owner = models.ForeignKey( User, related_name='job_owner',on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  jobtype = models.CharField(max_length=15 ,choices=Joptype)
  Description = models.TextField (max_length=1000)
  vacancy = models.IntegerField(default=1)
  published_at = models.DateTimeField(auto_now=True)
  salary = models.IntegerField(default=0)
  experience = models.IntegerField(default=1)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  image = models.ImageField (upload_to=image_upload)
  slug = models.SlugField(null=True , blank=True , unique=True)
  def __str__  (self):
    return self.title
  
  def save(self,*args,**kwargs):
     self.slug = slugify(self.title)
     super(Job,self).save(*args,**kwargs)
  
class Category (models.Model):
  name = models.CharField(max_length=15)

  def __str__ (self):
    return self.name
  
class Apply (models.Model):
  job = models.ForeignKey(Job , related_name= 'apply_job', on_delete=models.CASCADE)
  name =models.CharField( max_length=50)
  email = models.EmailField(max_length=100)
  website = models.URLField()
  cv = models.FileField(upload_to='apply/')
  cover_letter = models.TextField ( max_length=500)
  created_at = models.DateTimeField(auto_now=True)

  def __str__ (self):
    return self.name 