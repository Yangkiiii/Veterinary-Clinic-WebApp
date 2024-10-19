from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        # Retrieve form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        number = request.POST.get('phone')
        address = request.POST.get('address')
        confirm_password = request.POST.get('confirm_password')

        # Password confirmation check
        if password != confirm_password:
            return render(request, 'reg.html', {'error': 'Passwords do not match'})

        # Save the new account to the database
        new_account = Accounts(
            email=email,
            password=password,  # Hash password
            fname=first_name,
            lname=last_name,
            number=number,
            address=address
        )
        new_account.save()  # Save to database
        

        # Redirect to home or another page after successful registration
        return redirect('index')

    return render(request, 'reg.html')


def forgot(request):
    return render(request, 'forgotPass.html')

def mail(request):
    email = request.GET.get('email', '')
    return render(request, 'mail.html', {'email': email})

def admin(request):
    
    return render(request, 'AppointSched.html')
        


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

