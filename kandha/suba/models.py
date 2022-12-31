from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

# Create your models here.
class catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    number=models.CharField(max_length=30)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")

    submission_date=models.DateTimeField()
    year_old=models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class service(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    service_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    service_cost=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")

    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
        
class Cart(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.service.service_cost