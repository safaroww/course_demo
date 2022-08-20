from turtle import title
from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title



class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rank = models.IntegerField()
    tag = models.ManyToManyField(Tag)
    price = models.FloatField()
    image = models.ImageField(upload_to='course_image/')

    def __str__(self):
        return self.title
    



class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField(max_length=300)
    view_count = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title