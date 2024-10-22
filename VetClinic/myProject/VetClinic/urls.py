from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('registration/', views.registration, name='registration'),  
    path('forgot-password/', views.forgot, name='forgot'),  
    path('Appointment-Schedule/', views.admin, name='admin'),  
    path('Client-Records/', views.vet, name='vet'),  
    path('Transaction-History/', views.trans, name='trans'),  
    path('form/', views.form, name='form'),  
    path('Change-password/', views.change, name='change'),  
    path('Homepage/', views.owner, name='owner'),  
    path('profile/', views.profile, name='profile'),  
    path('MyHistory/', views.ownhistory, name='ownhistory'), 
    path('Appointment/', views.appwindow, name='appwindow'),  
    path('Admin-History/', views.adhistory, name='adhistory'),  
    path('Account-History/', views.adaccount, name='adaccount'),  
    path('mail/', views.mail, name= 'mail'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
