from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('forgot', views.forgot, name="forgot"),
    path('mail', views.mail, name="mail"),
    path('admin', views.admin, name="admin"),
    path('adhistory', views.adhistory, name="adhistory"),
    path('adaccount', views.adaccount, name="adaccount"),
    path('vet', views.vet, name="vet"),
    path('trans', views.trans, name="trans"),
    path('form', views.form, name="form"),
    path('change', views.change, name="change"),
    path('owner', views.owner, name="owner"),
    path('ownhistory', views.ownhistory, name="ownhistory"),
    path('appwindow', views.appwindow, name="appwindow"),

]