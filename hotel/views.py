from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout
from .models import *

# Create your views here.

def index(request):

    context = {
        'u_name': User

    }
    return render(request, 'index.html', context)


def rooms(request):
    room = roomtype.objects.all()
    context = {
        'room': room
    }
    return render(request, 'rooms.html', context)


def detail(request, type):
    r = room.objects.all()
    context = {
        'rooms': r,
        'type' : type
    }

    return render(request, 'detail.html', context)


def login(request):
    if request.method == 'POST':
        u_name = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=u_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "incorrect Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        u_name = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['cpass']
        if f_name != "" and l_name != "" and email != "" and pass1 != "" and pass2 != "":
            if pass1 == pass2:
                if User.objects.filter(username=u_name).exists():
                    messages.info(request, 'User Name Exist')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=u_name, password=pass1, email=email, first_name=f_name,
                                                    last_name=l_name)
                    user.save()
                    return redirect('/')
        else:
            messages.info(request, 'please Fill Form Completely')
            return redirect('register')
    return render(request, 'register.html')


def booking(request):
    if request.method == 'POST':
        ddate = request.POST['d_date']
        room = request.POST['room_type']

        reservations = reservation.objects.all()
        for res in reservations:
            res_room = res.room_type
            print(res_room)
            print(room)

            if res_room == room:
                print(room)
                print(res.room_type)
                if res.departure_date == ddate:
                    context = {
                        'msg' == "Not Available Choose another room"
                    }
                    return render(request, 'index.html', context)

    return render(request, 'booking.html')


def book(request):
    if request.method == 'POST':
        room = request.POST['room_type']
        adate = request.POST['a_date']
        ddate = request.POST['d_date']
        totalguest = request.POST['guest_adult'] + " Adult " + request.POST['guest_childrens'] + " Childrens"
        password = request.POST['pass']

        if auth.authenticate(username=request.user, password=password):
            r = reservation(user=request.user, room_type=room, arrival_date=adate, departure_date=ddate, guest=totalguest)
            r.save()
            return redirect("/")
        messages.info(request, 'Password is Wrong')
        return redirect('booking')
    return render(request, 'booking.html')



def account(request):
    r = reservation.objects.all()
    
    context = {
        'bookings': r
    }

    return render(request, 'account.html', context)


def profile(request):
    return render(request, 'profile.html')


def log_out(request):
    logout(request)
    return redirect('/')
