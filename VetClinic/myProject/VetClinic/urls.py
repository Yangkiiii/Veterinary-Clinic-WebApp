from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page (login)
    path('registration/', views.registration, name='registration'),  # User registration
    path('forgot-password/', views.forgot, name='forgot'),  # Password recovery
    path('Appointment-Schedule/', views.admin, name='admin'),  # Admin login handling
    path('Client-Records/', views.vet, name='vet'),  # Veterinarian dashboard
    path('Transaction-History/', views.trans, name='trans'),  # Transaction history
    path('form/', views.form, name='form'),  # Form submission
    path('Change-password/', views.change, name='change'),  # Change password
    path('Homepage/', views.owner, name='owner'),  # Owner details
    path('profile/', views.profile, name='profile'),  # User profile
    path('MyHistory/', views.ownhistory, name='ownhistory'),  # Owner's history
    path('Appointment/', views.appwindow, name='appwindow'),  # Application window
    path('Admin-History/', views.adhistory, name='adhistory'),  # Admin history
    path('Account-History/', views.adaccount, name='adaccount'),  # Admin account management
    path('mail/', views.mail, name= 'mail'),
]
