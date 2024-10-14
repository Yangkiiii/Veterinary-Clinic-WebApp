from django.db import models

class Accounts(models.Model):
    email = models.EmailField(max_length=30, unique=True, verbose_name='Email')
    password = models.CharField(max_length=30, verbose_name='Password')
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')  # Fixed spacing
    number = models.CharField(max_length=15, verbose_name='Phone Number')  # Fixed spacing
    address = models.TextField(verbose_name='Address')

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"


class Schedule(models.Model):
    owners_name = models.CharField(max_length=30, unique=True, verbose_name='Owners Name')
    species_id = models.IntegerField(verbose_name='Species ID')
    services_id = models.IntegerField(verbose_name='Services ID')
    date_time = models.DateTimeField(null=True,verbose_name='Date/Time')  # Use DateTimeField for both date and time
    status = models.CharField(max_length=30, verbose_name='Status')
    payment_status = models.CharField(max_length=15, verbose_name='Payment Status')

    def __str__(self):
        return f"Owner: {self.owners_name}, Species ID: {self.species_id}, Date: {self.date_time}"


class TransactionHistory(models.Model):
    date = models.CharField(max_length=30, unique=True, verbose_name='Date')
    amount = models.IntegerField(verbose_name='Amount')
    user_id = models.IntegerField(verbose_name='User ID')  # Changed to lowercase for consistency
    service = models.CharField(max_length=30, verbose_name='Services')
    pet_species = models.CharField(max_length=30, verbose_name='PetSpecies')

    def __str__(self):
        return f"Date: {self.date}, Amount: {self.amount}, User ID: {self.user_id}, Service: {self.service}, Pet Species: {self.pet_species}"


class Services(models.Model):
    type_of_services = models.CharField(max_length=30, unique=True, verbose_name='Type of Services')  # Changed to lowercase
    price = models.IntegerField(verbose_name='Price')

    def __str__(self):
        return f"Service: {self.type_of_services}, Price: {self.price}"  # Fixed missing parentheses


class Animal(models.Model):
    pet_species = models.CharField(max_length=30, unique=True, verbose_name='Pet Species')  # Changed to lowercase

    def __str__(self):
        return f"Pet Species: {self.pet_species}"


class AvailableSlot(models.Model):
    available_slot_time = models.CharField(max_length=30, unique=True, verbose_name='Available Slot Time')  # Fixed to CharField
    slot_left = models.IntegerField(verbose_name='Slot Left')  # Changed to lowercase

    def __str__(self):
        return f"Available Time: {self.available_slot_time}, Slots Left: {self.slot_left}"  # Fixed missing parentheses
