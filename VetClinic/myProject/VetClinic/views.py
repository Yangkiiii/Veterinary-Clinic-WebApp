from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Accounts

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        # Check if the account exists
        try:
            account = Accounts.objects.get(email=email)
        except Accounts.DoesNotExist:
            return render(request, 'login.html', {
                'error_message': 'Invalid email or password.'
            })

        # Verify the password
        if account.password == password:  # Directly check the stored plain password
            request.session['fname'] = account.fname
            request.session['email'] = account.email  # Store the email in the session
            return redirect('owner')
        else:
            return render(request, 'login.html', {
                'error_message': 'Invalid email or password.'
            })

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        # Retrieve form data
        email = request.POST.get('email').strip()  # Strip leading/trailing spaces
        password = request.POST.get('password')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        number = request.POST.get('phone')
        address = request.POST.get('address')
        confirm_password = request.POST.get('confirm_password')

        # Check for password confirmation
        if password != confirm_password:
            return render(request, 'reg.html', {'error': 'Passwords do not match'})

        # Create the new account
        new_account = Accounts(
            email=email,
            password=password,  # Store the plain password
            fname=first_name,
            lname=last_name,
            number=number,
            address=address,
        )
        new_account.save()

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('index')  # Redirect to the login page after registration

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
