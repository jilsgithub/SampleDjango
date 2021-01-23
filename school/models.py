from django.db import models

# Create your models here.
class Student(models.Model):
    stname = models.CharField(max_length=20)
    place  = models.CharField(max_length=10)
    mark   = models.IntegerField(default=50)

    def __str__(self):
        return(self.stname+': '+self.place+\
         ': '+str(self.mark))
