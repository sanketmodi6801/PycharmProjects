from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    # return HttpResponse("In the project")
    return render(request, 'index.html')


def signup(request):
    print(request.method)
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Account created")
        return render(request, 'index.html')

    else:
        return HttpResponse("404 - Not found")


def Login(request):
    print(request.method)
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        print(loginusername, loginpassword)

        User = authenticate(username=loginusername, password=loginpassword)
        if User is not None:
            login(request, User)
            messages.success(request, "Successfully Logged In")
            return redirect('/shop')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')



