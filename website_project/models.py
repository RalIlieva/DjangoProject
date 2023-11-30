from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Contact(models.Model):
    full_name = models.CharField(max_length=80)
    position_description = models.TextField()
    email = models.EmailField(max_length=80)

    def __str__(self):
        return self.full_name
