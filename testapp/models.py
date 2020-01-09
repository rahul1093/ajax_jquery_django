from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class StudentData(models.Model):
    Firstname = models.CharField(max_length=50)
    Middlename = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    SSC_marks = models.IntegerField()
    Diploma_marks = models.IntegerField()
    BE_marks = models.IntegerField()
    Email = models.EmailField(max_length=50)
    contact = models.IntegerField()
