from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("pricing/",views.pricing,name="pricing"),
    path("services/",views.services,name="services"),
    path("faq/",views.faq, name="faq"),
    path("contact/",views.contact,name="contact"),
    path("designs/",views.designs,name="designs"),
    path("reviews/",views.reviews,name="reviews")
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)