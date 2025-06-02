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
        return f"{self.name} - {self.rating}"
    
    
class InvitationDesign(models.Model):
    CATEGORY_CHOICES = [
        ('classic', 'Classic'),
        ('modern', 'Modern'),
        ('themed', 'Themed'),
    ]

    title = models.CharField(max_length=200, blank=True)
    get_image = models.ImageField(upload_to='invitations/', null=True, blank=True)  # uploaded image
    image_url = models.URLField(blank=True, null=True)  # external image link
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or "Untitled Design"
    
    def get_image_url(self):
        """Return the URL for the image."""
        if self.get_image:
            return self.get_image.url
        return ''

    class Meta:
        ordering = ['created_at']
