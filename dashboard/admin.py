from django.contrib import admin
from .models import ContactForm,Service,InvitationDesign
# Register your models here.

admin.site.register(ContactForm)
admin.site.register(Service)

from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(InvitationDesign)
class InvitationDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')