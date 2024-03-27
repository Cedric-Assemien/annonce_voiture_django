from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Ad(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    user = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    image = models.ImageField(upload_to="annonce", default="null")
    description = models.TextField(max_length=1000)
    state = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    def __str__(self):
        return self.first_name
    



    

