from django.db import models
from category.models import Category
# Create your models here.

class Task(models.Model):
    task_title=models.CharField(max_length=50)
    task_description=models.TextField()
    task_category=models.ManyToManyField(Category) 
    task_assign_date = models.DateField()  # Field for assigning a date
    task_is_complete = models.BooleanField(default=False)  # Field for completion status

    def __str__(self):
        return f'{self.task_title}'
    