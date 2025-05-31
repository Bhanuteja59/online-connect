from django.contrib import admin
from .models import ContactForm,Service
# Register your models here.

admin.site.register(ContactForm)
admin.site.register(Service)

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at')
    readonly_fields = ('created_at',)