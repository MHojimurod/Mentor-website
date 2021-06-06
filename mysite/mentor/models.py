from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Trainers(models.Model):
    full_name = models.CharField(max_length=120, blank=False, null=False)
    image = models.ImageField(upload_to='images/',blank=False, null=False)
    description = models.TextField(blank=False,null=False)
    instagram = models.URLField(blank=False, null=False)
    telegram = models.URLField(blank=False, null=False)
    facebook = models.URLField(blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='images/',blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    vote = models.PositiveIntegerField(blank=True, null=True)
    schedule = models.TextField(max_length=120, blank=False, null=False)
    seates = models.PositiveIntegerField( blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)
    trainer = models.ForeignKey(Trainers, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=120,blank=False,null=False)
    email_user = models.EmailField(max_length=120,blank=False,null=False)
    subject = models.CharField(max_length=120,blank=False,null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Newsletter(models.Model):
    email = models.EmailField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Events(models.Model):
    title = models.CharField(max_length=120,blank=False,null=False)
    image = models.ImageField(upload_to='images/',blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

