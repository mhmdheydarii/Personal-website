from django.db import models
from django.core.validators import EmailValidator
from .vlidators import validate_iranian_cellphone_number
# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="project/")
    description = models.TextField()
    skill = models.ManyToManyField(Skill, related_name="posts")
    address = models.URLField(max_length=300, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number])
    message = models.TextField()

    is_seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_date"]
