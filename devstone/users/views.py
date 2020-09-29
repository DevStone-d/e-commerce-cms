from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Account
# Create your views here.


def index(request):
    return HttpResponseRedirect(reverse('users:profile'))

def profile(request):
    '''
        Ahmet
        Deger
        5312829809
        1998-01-22
        0
    '''
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST["gender"]
        print(first_name)
        print(last_name)
        print(phone)
        print(date_of_birth)
        print(gender)

        print(request.user.date_of_birth)


        currentUser = Account.objects.get(pk=request.user.id)
        currentUser.first_name = first_name
        currentUser.last_name = last_name
        currentUser.phone = phone
        currentUser.date_of_birth = date_of_birth
        currentUser.gender = gender
        print(currentUser.date_of_birth)
        currentUser.save()

        return HttpResponseRedirect(reverse('users:profile'))
    else:
        currentUser = Account.objects.get(pk=request.user.id)
        xmonth = int(currentUser.date_of_birth.month)

        if xmonth < 10:
            xmonth = "0" + str(xmonth)

        return render(request, 'users/profile.html',{
            "xmonth" : xmonth
        })

def orders(request):
    return render(request, 'users/orders.html')

def reviews(request):
    return render(request, 'users/reviews.html')

def adress(request):
    return render(request, 'users/adress.html')

def changePass(request):
    if request.method == "POST":
        prevpassword = request.POST["prevpassword"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        is_valid = authenticate(request, username=request.user.email, password=prevpassword)
        currentUser = Account.objects.get(pk=request.user.id)
        xmonth = int(currentUser.date_of_birth.month)

        if xmonth < 10:
            xmonth = "0" + str(xmonth)

        if is_valid is None :
            return render(request, "users/profile.html", {
                "message": "Girdiginiz sifre yanlis.",
                "xmonth" : xmonth
            })
        elif password != confirmation:
            return render(request, "users/profile.html", {
                "message": "Şifreler uyuşmuyor.",
                "xmonth" : xmonth
            })
        elif prevpassword == password :
            return render(request, "users/profile.html", {
                "message": "Eski sifre ile yeni sifre ayni olamaz.",
                "xmonth" : xmonth
            }) 
        else:
            currentUser = Account.objects.get(pk=request.user.id)
            currentUser.set_password(password)
            currentUser.save()
            return HttpResponseRedirect(reverse('home:index'))
    else:
        return HttpResponseRedirect(reverse('users:profile'))
