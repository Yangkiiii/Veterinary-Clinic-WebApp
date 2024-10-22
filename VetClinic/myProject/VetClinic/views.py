from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.hashers import make_password


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using Django's built-in method
        account = authenticate(request, username=email, password=password)

        if account is not None:
            # Log in the user
            login(request, account)

            # Redirect based on the user's role
            if hasattr(account, 'role'):  # Check if the account has a role attribute
                if account.role == 'admin':
                    return redirect('admin')  # Redirect to admin page
                elif account.role == 'vet':
                    return redirect('vet')  # Redirect to vet page
                else:
                    return redirect('change')  # Redirect for other roles
            else:
                messages.error(request, 'User role not found')
                return redirect('index')  # Redirect back to the login page

        else:
            # Show an error message if authentication fails
            messages.error(request, 'Invalid email or password')
            return redirect('index')  # Redirect back to the login page

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

        
        if password != confirm_password:
            return render(request, 'reg.html', {'error': 'Passwords do not match'})

       
        new_account = Accounts(
            email=email,
            password=password,  
            fname=first_name,
            lname=last_name,
            number=number,
            address=address
        )
        new_account.save()  
        

        
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

