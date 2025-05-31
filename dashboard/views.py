from django.shortcuts import render,redirect
from .models import ContactForm,Service, InvitationDesign
from django.utils import timezone
from .models import Review
from .forms import ReviewForm



def dashboard(request):
        
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        wedding_date = request.POST.get('weddingDate')
        message = request.POST.get('message')

        contact = ContactForm(
            username=username,
            email=email,
            phonenumber=phonenumber,
            wedding_date=wedding_date,
            message=message,
            datetime=timezone.now()
        )
        contact.save()
        return render(request, "dashboard.html", {"success": True})
    
    return render(request, "dashboard.html")



def pricing(request):
    return render(request, "pricing.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        wedding_date = request.POST.get('weddingDate')
        message = request.POST.get('message')

        contact = ContactForm(
            username=username,
            email=email,
            phonenumber=phonenumber,
            wedding_date=wedding_date,
            message=message,
            datetime=timezone.now()
        )
        contact.save()
        return render(request, "contact.html", {"success": True})
    
    return render(request, "contact.html")

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})





def designs(request):
    # Fetch all invitation designs from the database
    designs = InvitationDesign.objects.all()

    # Group designs by category (optional for tab filtering)
    categories = InvitationDesign.CATEGORY_CHOICES

    return render(request, "designs.html", {'designs': designs, 'categories': categories})






def reviews(request):
    reviews = Review.objects.order_by('-created_at')[:10]  # Show last 10 reviews
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        
        

    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})
