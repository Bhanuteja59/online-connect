from django.db import models
from django.utils import timezone


class ContactForm(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phonenumber = models.CharField(max_length=15)
    wedding_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.email}"



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(help_text="Paste a direct image URL (GIF, PNG, JPG, etc.)")

    def __str__(self):
        return self.title
    


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField(default=5)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.rating}/5"