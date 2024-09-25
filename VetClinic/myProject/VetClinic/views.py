from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'reg.html')

def forgot(request):
    return render (request, 'forgotPass.html')

def mail (request):
    return render(request, 'mail.html')

def admin(request):
    return render(request, "AppointSched.html")

def adhistory(request):
    return render(request, "AccountHistory.html")

def adaccount(request):
    return render(request, "AccountHistory.html")

def vet(request):
    return render(request, "VetWindow.html")

def trans(request):
    return render(request, "transaction_history.html")

def form(request):
    return render(request, "DiagnosisForm.html")

def change(request):
    return render(request, "changepass.html")

def owner(request):
    return render(request, "homepage.html")

def profile(request):
    return render(request, "profile.html")

def ownhistory(request):
    return render(request, "TransactionHistoryPetOwner.html")

def appwindow(request):
    return render(request, "AppointmentWindow.html")
