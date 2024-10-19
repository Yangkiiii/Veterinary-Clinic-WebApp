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
            # Save the account using the form's save method
            account = form.save(commit=False)
            account.set_password(form.cleaned_data['password'])  # Hash the password
            account.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('index')  # Redirect to the index or another page after registration
    else:
        form = RegistrationForm()

    return render(request, 'reg.html', {'form': form})

@login_required
def owner(request):
    user = request.user  # Get the logged-in user
    print(f"Logged in user: {user.username}")

    try:
        # Assuming Accounts has a OneToOne relation with User
        account = Accounts.objects.get(user=user)
        first_name = account.first_name  # Correct field name
        print(f"First Name: {first_name}")
    except Accounts.DoesNotExist:
        first_name = None
        print("No account found for this user.")

    return render(request, "homepage.html", {  # Assuming you want to render homepage
        'fname': first_name
    })

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Retrieve user account details
            account = Accounts.objects.get(email=user.email)
            request.session['fname'] = account.fname
            request.session['lname'] = account.lname

            # Redirect users based on their role
            if user.is_superuser:
                return JsonResponse({'success': True, 'redirect_url': '/admin/'})
            else:
                return JsonResponse({'success': True, 'redirect_url': request.META.get('HTTP_REFERER', '/')})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email or password'})
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})





def public_view(request):
    return render(request, 'login.html')


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

