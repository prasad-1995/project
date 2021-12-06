from .serializers import Userserializer
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from client.models import Client


# Create your views here.


@api_view(['GET', 'POST'])
def user(request):
    if request.method == 'GET':
        users = User.objects.all()
        UserSerializer = Userserializer(users, many=True)
        return Response(UserSerializer.data)

    elif request.method == 'POST':
        UserSerialize = Userserializer(data=request.data)
        if UserSerialize.is_valid():
            UserSerialize.save()
            return Response(UserSerialize.data)
        else:
            return Response(UserSerialize.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def clientDetailView(request, pk):
    try:
        usr = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=404)

    if request.method == "DELETE":
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "GET":
        serializer = Userserializer(usr)
        return Response(serializer.data)

    elif request.method == "PUT":
        userSerializer = Userserializer(usr, data=request.data)
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(userSerializer.data)
        else:
            return Response(userSerializer.errors)


def home(request):
    return render(request, './home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in successfully')
            return redirect('dashboard')

        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # print("Hello we get post message")
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist')
                    return redirect('register')

                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                                    username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are logged in successfully')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, "You are registered successfully")
                    return redirect('login')

        else:
            messages.error(request, "password do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')


@login_required(login_url='login')
def dashboard(request):
    clients = Client.objects.all()
    data = {
        'cl': clients
    }
    return render(request, 'dashboard.html', data)
    # return render(request, 'home.html', data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return redirect('home')
