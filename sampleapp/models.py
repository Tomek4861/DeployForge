from django.db import models


class ContactFormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)
    created_date = models.DateField(auto_now_add=True)
