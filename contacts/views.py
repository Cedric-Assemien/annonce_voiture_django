from django.shortcuts import render, redirect
from django.contrib import messages
from contacts.models import User,Ad
from django.contrib.auth.models import User


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        image = request.POST.get('image')
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        car_title = request.POST.get('car_title')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_need = request.POST.get('customer_need')
        city = request.POST.get('city')
        state = request.POST('state')
        email = request.POST.get('email')
        
        contact = Ad(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message,image=image,
        name=name,subject=subject)
        contact.save()
        messages.success(request, 'Félicitation, vous avez soumis l\'annonce avec succés')
        return redirect('/cars/'+car_id)

def contact(request):
    
    user = request.user
    User.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('image')       
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        email_subject = 'Vous avez un nouveau message  ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
       

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        ad = Ad()
        ad.title = name
        ad.image = image
        ad.email = email         
        ad.phone = phone
        ad.autor = user 
        ad.subject = subject
        ad.message = message
        ad.save()

        messages.success(request, 'Félicitation, vous avez soumis l\'annonce avec succés')
        return redirect('contact')

    return render(request, 'pages/contact.html')