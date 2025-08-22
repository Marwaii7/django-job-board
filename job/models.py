from django.db import models



Joptype=(
  ('part time' , 'part time'),
  ('Full time' , 'Full time'),
)
# Create your models here.
class Job (models.Model):
  title = models.CharField(max_length=100)
  jobtype = models.CharField(max_length=15 ,choices=Joptype)
  Description = models.TextField (max_length=1000)
  vacancy = models.IntegerField(default=1)
  published_at = models.DateTimeField(auto_now=True)
  salary = models.IntegerField(default=0)

  def __str__  (self):
    return self.title