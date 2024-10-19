from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CustomLoginForm
from .forms import RegistrationForm

def index(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Hash the password before saving
            account = form.save(commit=False)
            account.password = make_password(form.cleaned_data['password'])
            account.save()
            return redirect('index')  # Redirect to the index or another page after registration
    else:
        form = RegistrationForm()
    
    return render(request, 'reg.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect users based on their role
            if user.is_superuser:
                return JsonResponse({'success': True, 'redirect_url': '/admin/'})
            else:
                return JsonResponse({'success': True, 'redirect_url': '/vet/'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email or password'})
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


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

