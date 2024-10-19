from django.db import models


class Accounts(models.Model):  # Singular for model names is recommended
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    password = models.CharField(max_length=128, verbose_name='Password')  # 128 for hashed passwords
    fname = models.CharField(max_length=30, verbose_name='First Name')
    lname = models.CharField(max_length=30, verbose_name='Last Name')
    number = models.CharField(max_length=15, verbose_name='Phone Number')  # Improved verbose_name
    address = models.TextField(verbose_name='Address')

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.email})"


class Service(models.Model):
    type_of_service = models.CharField(max_length=30, unique=True, verbose_name='Type of Service')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')  # Use DecimalField for monetary values

    def __str__(self):
        return f"Service: {self.type_of_service}, Price: {self.price}"


class Animal(models.Model):  # Keep only one Animal model
    pet_species = models.CharField(max_length=30, unique=True, verbose_name='Pet Species')

    def __str__(self):
        return f"Pet Species: {self.pet_species}"


class AvailableSlot(models.Model):
    available_slot_time = models.DateTimeField(unique=True, verbose_name='Available Slot Time')  # Use DateTimeField for better time handling
    slots_left = models.IntegerField(verbose_name='Slots Left')

    def __str__(self):
        return f"Available Time: {self.available_slot_time}, Slots Left: {self.slots_left}"


class Schedule(models.Model):
    owners_name = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name="Owner's Name")  # Link to Account model
    species = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Species')  # Link to Animal model
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')  # Link to Service model
    date_time = models.DateTimeField(null=True, verbose_name='Date/Time')
    status = models.CharField(max_length=30, verbose_name='Status')
    payment_status = models.CharField(max_length=15, verbose_name='Payment Status')

    def __str__(self):
        return f"Owner: {self.owners_name.fname} {self.owners_name.lname}, Species: {self.species.pet_species}, Date: {self.date_time}"


class TransactionHistory(models.Model):
    date = models.DateField(verbose_name='Date')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, verbose_name='User')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')
    pet_species = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Pet Species')

    def __str__(self):
        return f"Date: {self.date}, Amount: {self.amount}, User: {self.user.fname} {self.user.lname}, Service: {self.service.type_of_service}, Pet Species: {self.pet_species.pet_species}"
