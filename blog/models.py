from django.db import models

sex_choices=(
     ('f','female'),
     ('m','male')
)

class Employee(models.Model):
     name=models.CharField(max_length=20)
     sex = models.CharField(max_length=20, choices=sex_choices)
     def __str__(self):
          return self.name

class Entry(models.Model):
     name=models.CharField(max_length=30)
     employee = models.ForeignKey(Employee)

     def __str__(self):
          return self.name

class Money(models.Model):
     name = models.CharField(max_length=20)
     emp = models.ManyToManyField(Employee)
     
     def __str__(self):
          return self.name
