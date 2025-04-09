from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    enrolled = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.age}'

