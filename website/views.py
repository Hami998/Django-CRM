from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

##Dodaj dijagrame potrosnje u aplikaciju!
##Dodaj listu da moze da se vidi kako trosis hranu, na koje namirnice se najvise hrane trosi
##Takodje ideja za BOLD projekat, ekonomska ideja, aplikacija koja ce pomoci gradjanima da
##sacuvaju novac, da vide gde najvise troskove imaju, da imaju uvid u svoje troskove, da imaju
##mogucnost da prave planove za buducnost, da imaju mogucnost da vide koliko su ustedeili
##na mesecnom nivou, da imaju mogucnost da prave planove za buducnost, da imaju mogucnost da

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error logging in. Please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')

