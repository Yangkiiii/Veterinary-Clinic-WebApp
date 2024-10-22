from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Accounts
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using Django's built-in method
        account = authenticate(request, username=email, password=password)

        if account is not None:
            # Log in the user
            login(request, account)

            # Redirect based on the user's role (admin, vet, or regular user)
            if hasattr(account, 'role'):
                if account.role == 'admin':
                    return redirect('admin')  # Redirect to admin page
                elif account.role == 'vet':
                    return redirect('vet')  # Redirect to vet page
                else:
                    return redirect('owner')  # Redirect for other roles (pet owner)
            else:
                messages.error(request, 'User role not found')
                return redirect('index')

        else:
            # Show an error message if authentication fails
            messages.error(request, 'Invalid email or password')
            return redirect('index')

    # If the user is authenticated, redirect to their homepage
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect('admin')
        elif request.user.role == 'vet':
            return redirect('vet')
        else:
            return redirect('owner')

    return render(request, 'homepage.html')  # Default login page


def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        number = request.POST.get('number')
        address = request.POST.get('address')
        password = request.POST.get('password')

        # Check if the email already exists
        if Accounts.objects.filter(email=email).exists():
            messages.warning(request, 'An account with this email already exists.')
            return redirect('registration')  # Redirect back to the registration page

        # Create new user if email is not taken
        Accounts.objects.create(
            email=email,
            fname=fname,
            lname=lname,
            number=number,
            address=address,
            password=password  # Remember you are storing plain text here
        )

        messages.success(request, 'Registration successful!')
        return redirect('index')  # Redirect to the index page or any other page

    return render(request, 'reg.html')

def custom_logout(request):
    logout(request)
    return redirect('index')



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
    if 'email' in request.session:
        email = request.session['email']
        try:
            account = Accounts.objects.get(email=email)
            if request.method == 'POST':
                # Update account information
                account.fname = request.POST.get('fname')
                account.lname = request.POST.get('lname')
                account.email = request.POST.get('email')
                account.address = request.POST.get('address')
                account.number = request.POST.get('phone')
                account.password = request.POST.get('password')  # Store the plain password cautiously

                account.save()  # Save changes to the database

                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')  # Redirect to the profile page after update

            # Render profile page with current account information
            context = {
                'first_name': account.fname,
                'last_name': account.lname,
                'email': account.email,
                'address': account.address,
                'phone_number': account.number,
                'password': account.password,  # Show password (consider security implications)
                'confirm_password': account.password,  # Confirm password (same as password)
            }
            return render(request, "profile.html", context)
        except Accounts.DoesNotExist:
            messages.error(request, 'Account not found. Please log in again.')
            return redirect('index')
    else:
        messages.error(request, 'You need to log in first.')
        return redirect('index')



def ownhistory(request):
    return render(request, "TransactionHistoryPetOwner.html")


def appwindow(request):
    return render(request, "AppointmentWindow.html")
