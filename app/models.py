from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    duedate = models.DateField(null=True, blank=True)
    remind = models.DateTimeField(null=True, blank=True)
    repeat = models.CharField(null=True, blank=True, max_length=120)
    file_id = models.ForeignKey('File', null=True, blank=True, on_delete=models.CASCADE, related_name='files')
    step_id = models.ForeignKey('AddStep', null=True, blank=True, on_delete=models.CASCADE, related_name='steps')
    category_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='categories')
    important = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class AddStep(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
CHOICES = (
    ('Blue Category', 'Blue Category'),
    ('Green Category', 'Green Category'),
    ('Red Category', 'Red Category'),
    ('Yellow Category', 'Yellow Category'),
    ('Purple Category', 'Purple Category'),
    ('Orange Category', 'Orange Category')
)
class Category(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    choice = models.CharField(choices=CHOICES, max_length=20)

    def __str__(self):
        return self.choice

class File(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    file = models.FileField()
