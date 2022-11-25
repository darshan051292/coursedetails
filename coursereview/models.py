from django.db import models

# Create your models here.

from django.db import models


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


class CourseDetails(models.Model):
    serial_no = models.IntegerField()
    course_title = models.ForeignKey('Course', on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    comments = models.TextField()


