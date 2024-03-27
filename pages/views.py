from django.shortcuts import render, redirect
from contacts.models import User,Ad
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def annonce(request):
    user = request.user
    annonces = Ad.objects.filter(autor = user)
    datas = {
        'annonces': annonces
    }
    return render(request,'annonce.html',datas)


def contact(request):
    
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('image')
        description=request.POST.get('description')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        

        email_subject = 'You have a new message from CarDealer Website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        ad = Ad()
        ad.title = name
        ad.image = image
        ad.email = email 
        ad.description = description
        ad.phone = phone
        ad.autor = user 
        ad.subject = subject
        ad.message = message
        ad.save()

        messages.success(request, 'Félicitation, vous avez soumis l\'annonce avec succés')
        return redirect('contact')

    return render(request, 'pages/contact.html')
