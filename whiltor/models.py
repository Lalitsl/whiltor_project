from django.db import models
import os
import datetime

def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)

class Card(models.Model):
    # img=models.CharField(max_length=100)
    img=models.ImageField(upload_to=filepath,null=True,blank=True)
    title=models.CharField(max_length=240,unique=True)
    data=models.CharField(max_length=240)

    def __str__(self):
        s=self.id,self.img,self.title,self.data
        return s

class achieve(models.Model):
    img1=models.ImageField(upload_to=filepath,null=True,blank=True)
    data1=models.CharField(max_length=240)

    def __str__(self):
        a=self.img1,self.data1
        return a
