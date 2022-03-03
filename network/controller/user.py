from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    return render(request, 'register.html')


def adduser(request):
    first = request.POST['fname']
    last = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confpassword = request.POST['confpassword']
    if confpassword == password:
        user = User.objects.create_user(
            first_name=first,
            last_name=last,
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('/iot_device')
    else:
        return redirect('/register')
