from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Account,Adress,Order
# Create your views here.

@login_required(login_url='home:login')
def index(request):
    return HttpResponseRedirect(reverse('users:profile'))

@login_required(login_url='home:login')
def profile(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST["gender"]

        currentUser = Account.objects.get(pk=request.user.id)
        currentUser.first_name = first_name
        currentUser.last_name = last_name
        currentUser.phone = phone
        currentUser.date_of_birth = date_of_birth
        currentUser.gender = gender
        currentUser.save()

        return HttpResponseRedirect(reverse('users:profile'))
    else:
        try:

            currentUser = Account.objects.get(pk=request.user.id)
            currentUser.date_of_birth.month

            xmonth = int(currentUser.date_of_birth.month)

            if xmonth < 10:
                xmonth = "0" + str(xmonth)

            return render(request, 'users/profile.html',{
                "xmonth" : xmonth
            })
        except AttributeError:
            return render(request, 'users/profile.html')

@login_required(login_url='home:login')
def orders(request):
    return render(request, 'users/orders.html')

@login_required(login_url='home:login')
def reviews(request):
    return render(request, 'users/reviews.html')

@login_required(login_url='home:login')
def adress(request):

    if request.method == "POST":
        user = Account.objects.get(pk=request.user.id)
        adress_first_name = request.POST["adress_first_name"]
        adress_last_name = request.POST["adress_last_name"]
        adress_phone = request.POST["adress_phone"]
        city = request.POST["city"]
        country = request.POST["country"]
        adresss = request.POST["adresss"]
        

        Adress(
            user=user,
            adress_first_name=adress_first_name,
            adress_last_name=adress_last_name,
            adress_phone=adress_phone,
            city=city,
            country=country,
            adresss=adresss
            ).save()

        return HttpResponseRedirect(reverse('users:adress'))

    else:
        user = Account.objects.get(pk=request.user.id)
        adress = Adress.objects.filter(user=user)
        return render(request, 'users/adress.html',{
            "useradress" : adress
        })

@login_required(login_url='home:login')
def adressdelete(request,id):
    
    pass

@login_required(login_url='home:login')
def changePass(request):
    if request.method == "POST":
        prevpassword = request.POST["prevpassword"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        is_valid = authenticate(request, username=request.user.email, password=prevpassword)
        currentUser = Account.objects.get(pk=request.user.id)
        try : 
            xmonth = int(currentUser.date_of_birth.month)
        except :
            xmonth = 0

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
