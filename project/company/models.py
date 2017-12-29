from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=100,default="")
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    exam = models.ForeignKey(Exam)

    def __str__(self):
        return self.question


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100,blank=False,default="")
    added_by = models.CharField(max_length=100)

    def __str__(self):
        return self.email
