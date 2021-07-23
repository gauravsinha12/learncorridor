from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def learn(request):
    return render(request,'learn.html')
def grow(request):
    return render(request,'grow.html')
def forms(request):
    return render(request,'forms.html')
def earn(request):
    return render(request,'earn.html')
def full(request):
    return render(request,'full.html')
def digital(request):
    return render(request,'digital.html')
def graphic(request):
    return render(request,'graphic.html')
def payout(request):
    return render(request,'pay.html')
def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        course = request.POST.get('course', '')
        if course == 'Digital Marketing':
            order = Orders(name=name, email=email, phone=phone,course=course,amount='799')
        elif course == 'Graphic Designing':
            order = Orders(name=name, email=email, phone=phone,course=course,amount='799')
        else:
            order = Orders(name=name, email=email, phone=phone,course=course,amount='3999')

        order.save()
        return render(request, '/')
    
    return render(request,'checkout.html')

def handleSignup(request):
    if request.method == 'POST':
        #taking values here
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #check for error inputs
        if len(username) > 10:
            messages.error(request, "Username should not be more than 10 characters.")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "username should be alpha numeric.")
            return redirect('/')
        if pass1 != pass2:
            messages.warning(request, "password didn't matched please try again.")
            return redirect('/')
        #user banega ab
        myuser = User.objects.create_user(username,email,pass1)
        myuser.phone_number = phone
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Signup succesfully')
        return redirect('/')
    else:
        return HttpResponse('404 - not found')
def handleLogin(request):
    if request.method == 'POST':
        #Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfull")
            return redirect('/')
        else:
            messages.warning(request, "wrong credentials, please try again")
            return redirect('/')

    return HttpResponse(request,"404 not found")
def handleLogout(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect('/')
def contact(request):
    if request.method == 'POST':
        #name = request.POST['name']
        #email = request.POST['email']
       # phone = request.POST['phone']
        desc = request.POST['desc']
    
        send_mail('contact',desc,settings.EMAIL_HOST_USER,['g1ur1vsinha@gmail.com'],fail_silently=False)

    return render(request, 'contact.html')