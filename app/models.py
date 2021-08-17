from django.db import models

# Create your models here.
class Entrys(models.Model):
    Name = models.CharField(max_length=23, null=False)
    Email = models.EmailField(unique=True)
    Message = models.CharField(max_length=255)
   
    def __str__(self):
       return self.Name
