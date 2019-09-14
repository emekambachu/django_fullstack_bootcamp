from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=246)

    def __str__(self):
        return self.name

    # redirect to details page, with contents that was just created
    def get_absolute_url(self):
        return reverse("cbvapp:detail", kwargs={'pk':self.pk})
        
    
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name