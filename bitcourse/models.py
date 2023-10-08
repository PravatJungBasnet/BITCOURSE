from django.db import models

# Create your models here.
class noticepart(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photo')
class notes(models.Model):
    title=models.CharField(max_length=40)
    note=models.FileField(upload_to='pdf')

